#!/usr/bin/env python3
"""
analyze_course.py — audit an audio course against its source document.

Compares the MP3s in reference/output/ against reference/input/original.pdf and
writes a report answering four questions:

  1. Do the audio files carry all the context from the original, without
     duplicating or padding it?
  2. Did the AI invent anything that is not in the original?
  3. What percentage of the original survives, and what exactly is missing?
  4. Is what survived arranged in a teachable way?

Pipeline
--------
  PDF  --pdftoppm+tesseract-->  source text  --clause split-->  claims
  MP3s --faster-whisper------>  lesson transcripts --sentence split--> units
  claims x units --MiniLM embeddings + lexical/entity checks--> coverage matrix
  coverage matrix --> deterministic findings
  (optional) source + transcripts --> Claude adjudication --> qualitative verdict

Everything expensive is cached under work/ so re-runs are cheap.

Runtime
-------
Transcription runs on faster-whisper/CTranslate2, which is already installed in the
phansora-api virtualenv on the server. Use that interpreter:

    /home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py

Device selection defaults to `auto`: if CTranslate2 reports a usable CUDA device the
job runs on GPU (float16 where supported), otherwise it runs on CPU (int8). A CUDA
load failure at runtime falls back to CPU rather than aborting the job. The same
WHISPER_* environment variables phansora-api reads are honoured here, so whatever is
already configured in prod carries over.

Check the box before committing to a long run:

    ... --check                 print resolved device/model/deps and exit

Usage
-----
  ... --no-llm                skip the Claude pass (deterministic report only)
  ... --device cuda|cpu|auto  override device selection
  ... --compute-type float16  override precision
  ... --whisper-model medium.en
  ... --force-ocr             redo OCR even if cached
  ... --force-transcribe      redo Whisper even if cached
  ... --audio-dir DIR --input-pdf FILE --work-dir DIR --out-dir DIR
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field, asdict
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Defaults assume the layout this script ships in; every one is overridable so the
# same script runs unchanged against a different tree in prod.
INPUT_PDF = HERE / "input" / "original.pdf"
AUDIO_DIR = HERE / "output"
WORK_DIR = HERE / "work"
OUT_DIR = HERE
REPORT_MD = OUT_DIR / "REPORT.md"
REPORT_JSON = OUT_DIR / "report.json"

# The audit reads the PDF. A corrected transcription is only used when passed
# explicitly with --source-text, which is the intended route after the OCR gate has
# rejected a page and a human has fixed it.
SIDECAR_SOURCE: Path | None = None

# Two independent gates on source-text quality. Below either one the report withholds
# coverage percentages rather than publishing a number that is really measuring OCR
# damage.
#
# Tesseract's own confidence is the weaker signal and must not be trusted alone: on
# this corpus it reported 87.9% mean word confidence for text where one lowercase word
# in six was not a real word (`chaque males all the differene` scored 92.4%). Dictionary
# validity is the signal that actually discriminates — a known-correct transcription of
# the same page scores 97.7%, the OCR of it scores 83.3%.
OCR_GATE = 85.0        # mean tesseract word confidence
LEX_GATE = 95.0        # share of lowercase word-tokens that are real words

# Front matter is not teaching content. A course that omits the copyright notice has
# not failed the listener, so scoring it as dropped content buries the findings that
# matter under boilerplate. Excluded statements are listed in the report, never
# silently dropped, and --keep-front-matter scores them like anything else.
# Match the legal furniture only. Loose patterns are worse than none here: a bare
# "copyright" also hits the source's disclosure that its images were edited and
# AI-generated, which is evidentiary rather than legal — a reader who sees it knows not
# to trust the pictures the lessons cite as proof — and "without consent" on its own
# hits "FREQUENCY IS THE ONLY THING THAT ENTERS YOUR TEMPLE WITHOUT CONSENT".
BOILERPLATE_PATTERNS = (
    r"registered with.{0,30}copyright",
    r"under the copyright of",
    r"all rights reserved",
    r"\bre-?sale\b",
    r"legal action",
    r"work title",
    r"\bisbn\b",
)

# A narrated word counts as lifted when it sits inside a run of at least this many
# consecutive words that also appear, in the same order, in the source. Eight is long
# enough that ordinary phrasing does not collide by chance and short enough to catch a
# copied sentence.
VERBATIM_SHINGLE = 8

DICT_PATHS = (
    "/usr/share/dict/british-english",     # first: 1940 English letter, "cheque"/"connexions"
    "/usr/share/dict/american-english",
    "/usr/share/dict/words",
)
_DICTIONARY: set[str] | None = None


def dictionary() -> set[str]:
    global _DICTIONARY
    if _DICTIONARY is not None:
        return _DICTIONARY
    words: set[str] = set()
    for p in DICT_PATHS:
        f = Path(p)
        if f.exists():
            for w in f.read_text(encoding="utf-8", errors="ignore").split():
                words.add(w.lower().strip("'"))
    _DICTIONARY = words
    return words


def lexical_validity(text: str) -> tuple[float, list[str]]:
    """Share of lowercase word-tokens that are real words, plus the offenders.

    Only lowercase tokens are judged: proper nouns legitimately miss from any word
    list, and penalising them would flag a correct transcription. The offender list
    doubles as a correction checklist for whoever fixes the text by hand.
    """
    words = dictionary()
    if not words:
        return -1.0, []                     # no wordlist on this box; gate disabled
    toks = re.findall(r"[A-Za-z][A-Za-z']{2,}", text)
    low = [t for t in toks if t.islower()]
    if not low:
        return 100.0, []
    bad = [t for t in low
           if t.lower().strip("'") not in words and t.lower().rstrip("s") not in words]
    return 100.0 * (1 - len(bad) / len(low)), sorted(set(bad))


def configure_paths(args) -> None:
    """Point the module at whatever tree this run should read and write."""
    global INPUT_PDF, AUDIO_DIR, WORK_DIR, OUT_DIR, REPORT_MD, REPORT_JSON, SIDECAR_SOURCE
    if args.input_pdf:
        INPUT_PDF = Path(args.input_pdf).resolve()
    if args.audio_dir:
        AUDIO_DIR = Path(args.audio_dir).resolve()
    if args.work_dir:
        WORK_DIR = Path(args.work_dir).resolve()
    if args.out_dir:
        OUT_DIR = Path(args.out_dir).resolve()
    if args.source_text:
        SIDECAR_SOURCE = Path(args.source_text).resolve()
    REPORT_MD = OUT_DIR / "REPORT.md"
    REPORT_JSON = OUT_DIR / "report.json"

# ---------------------------------------------------------------------------
# thresholds
# ---------------------------------------------------------------------------

COVERED_EMB = 0.60          # cosine sim above which a claim counts as covered
PARTIAL_EMB = 0.42          # ...and above which it counts as partial
COVERED_LEX = 0.55          # content-token F1 above which a claim counts as covered
PARTIAL_LEX = 0.35
NEAR_DUP_EMB = 0.82         # two output sentences this close say the same thing
UNGROUNDED_EMB = 0.38       # an output sentence this far from every claim is unsourced
ENTITY_FUZZ = 0.72          # name-match tolerance, to survive speech-recognition garble


# ---------------------------------------------------------------------------
# text utilities
# ---------------------------------------------------------------------------

STOPWORDS = {
    "a", "about", "above", "after", "again", "all", "also", "am", "an", "and", "any",
    "are", "as", "at", "be", "because", "been", "before", "being", "both", "but", "by",
    "can", "cannot", "could", "did", "do", "does", "doing", "down", "during", "each",
    "even", "for", "from", "further", "had", "has", "have", "having", "he", "her",
    "here", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its",
    "just", "me", "more", "most", "my", "no", "nor", "not", "of", "off", "on", "once",
    "only", "or", "other", "our", "out", "over", "own", "he", "same", "shall", "she",
    "should", "so", "some", "such", "than", "that", "the", "their", "them", "then",
    "there", "these", "they", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "we", "were", "what", "when", "where", "which",
    "while", "who", "whom", "why", "will", "with", "would", "you", "your",
}

# Scaffolding the course narrator adds on purpose. Sentences that are only
# scaffolding are not "fabrication" — they are pedagogy.
SCAFFOLD_PATTERNS = [
    r"^in this lesson\b", r"^this lesson\b", r"^this session\b", r"^to recap\b",
    r"^to recapat\b", r"^first,", r"^second,", r"^third,", r"^finally,",
    r"^the key point is\b", r"^in other words\b", r"^the source material\b",
    r"^drawing directly from\b", r"^he says\b", r"^he writes\b", r"^he states\b",
    r"^the author (says|writes|states|notes|explains)\b",
    r"^these are the only facts\b", r"^that is the scale\b",
]

WORD_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
}


def normalize_source(raw: str) -> str:
    """Unwrap the hard line breaks of a typed letter into flowing prose."""
    text = unicodedata.normalize("NFKC", raw)
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    # de-hyphenate words split across lines
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    # keep paragraph structure, collapse in-paragraph wrapping
    text = re.sub(r"\n\s*\n", "\n\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def tokens(text: str) -> list[str]:
    """Content tokens, crudely stemmed, stopwords dropped."""
    words = re.findall(r"[a-z0-9']+", text.lower())
    out = []
    for w in words:
        w = w.strip("'")
        if not w or w in STOPWORDS or len(w) < 2:
            continue
        for suf in ("ing", "ed", "es", "s"):
            if len(w) > 4 and w.endswith(suf):
                w = w[: -len(suf)]
                break
        out.append(w)
    return out


def token_f1(a: list[str], b: list[str]) -> float:
    """Overlap of a's content against b, weighted toward recall of a."""
    if not a:
        return 0.0
    sa, sb = set(a), set(b)
    hits = len(sa & sb)
    if not hits:
        return 0.0
    recall = hits / len(sa)
    precision = hits / max(len(sb), 1)
    return (2 * recall * precision) / (recall + precision) if (recall + precision) else 0.0


def numbers_in(text: str) -> set[str]:
    """Numeric facts, whether written as digits or words."""
    found: set[str] = set()
    for m in re.findall(r"\d+", text):
        found.add(str(int(m)))
    low = text.lower()
    words = re.findall(r"[a-z]+", low)
    i = 0
    while i < len(words):
        w = words[i]
        if w in WORD_NUMBERS:
            val = WORD_NUMBERS[w]
            # "thirty pounds", "twenty five"
            if i + 1 < len(words) and words[i + 1] in WORD_NUMBERS:
                nxt = WORD_NUMBERS[words[i + 1]]
                if val >= 20 and nxt < 10:
                    val += nxt
                    i += 1
            found.add(str(val))
        i += 1
    return found


def entities_in(text: str, is_source: bool) -> set[str]:
    """Proper-noun-ish tokens: capitalised words and dotted abbreviations."""
    out: set[str] = set()
    for m in re.findall(r"\b(?:[A-Z]\.){2,}[A-Z]?\b", text):          # O.T.O., G.M.C.
        out.add(re.sub(r"[^A-Za-z]", "", m).upper())
    for m in re.findall(r"\b[A-Z][a-z]{2,}\b", text):
        if m.lower() in STOPWORDS:
            continue
        out.add(m.upper())
    # sentence-initial capitals are noise, not names
    first = re.match(r"\s*([A-Z][a-z]{2,})", text)
    if first and not is_source:
        out.discard(first.group(1).upper())
    return out


def spoken_in(entity: str, text: str) -> bool:
    """Is this name present in `text`, ignoring case?

    Both sides of the comparison extract entities by capitalisation, which is a fair
    rule for a typescript and a bad one for a transcript: Whisper's casing is
    arbitrary (lesson 01 writes "Tarot", lesson 03 writes "tarot" throughout). Without
    this fallback a near-verbatim quote reads as a dropped detail, and a word the
    letter happens to lowercase reads as course invention.
    """
    word = entity.lower()
    if re.search(rf"\b{re.escape(word)}\b", text.lower()):
        return True
    # O.T.O. / OTO / o.t.o. are the same name. Compared as whole tokens, not as a
    # substring of the de-punctuated text, where "one" would hide inside "money".
    dotted = re.findall(r"\b(?:[A-Za-z]\.){2,}[A-Za-z]?\b", text)
    return word in {re.sub(r"[^a-z]", "", m.lower()) for m in dotted}


def entity_matches(needle: str, haystack: set[str]) -> bool:
    """Fuzzy name match — speech recognition mangles proper nouns badly."""
    if needle in haystack:
        return True
    for cand in haystack:
        if SequenceMatcher(None, needle, cand).ratio() >= ENTITY_FUZZ:
            return True
        if len(needle) >= 4 and len(cand) >= 4 and needle[:4] == cand[:4]:
            return True
    return False


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", text)
    out = []
    for p in parts:
        p = p.strip()
        if len(p) > 1:
            out.append(p)
    return out


def is_scaffold(sentence: str) -> bool:
    low = sentence.strip().lower()
    return any(re.search(p, low) for p in SCAFFOLD_PATTERNS)


def is_boilerplate(text: str) -> bool:
    low = text.lower()
    return any(re.search(p, low) for p in BOILERPLATE_PATTERNS)


def bare_words(text: str) -> list[str]:
    """Word stream with casing and punctuation removed.

    The source is upper-case with OCR punctuation; the transcript is prose. Comparing
    them for copying has to happen below that difference or nothing matches.
    """
    return re.findall(r"[a-z0-9']+", text.lower())


def verbatim_runs(source: str, lessons: list[tuple[str, str]], n: int):
    """Find narration lifted word-for-word from the source.

    Coverage answers 'is the content there'. This answers the opposite question: is it
    there *in the source's own words*. A course can score high on the first by simply
    reading the book aloud, which is what this is meant to catch. Returns per-lesson
    stats and every run, longest first.

    Note when reading the output: the source quotes scripture, so a course quoting the
    same verse produces a run here without having copied the source's own writing.
    """
    src = bare_words(source)
    index: dict[tuple, list[int]] = {}
    for i in range(len(src) - n + 1):
        index.setdefault(tuple(src[i:i + n]), []).append(i)

    per_lesson = []
    runs: list[tuple[int, str, str]] = []      # (length, lesson, text)
    total_words = total_lifted = 0

    for lesson, text in lessons:
        nar = bare_words(text)
        covered = [False] * len(nar)
        longest = 0
        j = 0
        while j <= len(nar) - n:
            key = tuple(nar[j:j + n])
            starts = index.get(key)
            if not starts:
                j += 1
                continue
            best = 0
            for start in starts:
                k = n
                while (j + k < len(nar) and start + k < len(src)
                       and nar[j + k] == src[start + k]):
                    k += 1
                best = max(best, k)
            for t in range(j, j + best):
                covered[t] = True
            runs.append((best, lesson, " ".join(nar[j:j + best])))
            longest = max(longest, best)
            j += best

        lifted = sum(covered)
        total_words += len(nar)
        total_lifted += lifted
        per_lesson.append({
            "lesson": lesson,
            "words": len(nar),
            "lifted": lifted,
            "percent": pct(lifted, len(nar)),
            "longest_run": longest,
        })

    runs.sort(key=lambda r: -r[0])
    return {
        "shingle": n,
        "percent": pct(total_lifted, total_words),
        "words": total_words,
        "lifted": total_lifted,
        "per_lesson": per_lesson,
        "runs": [{"length": l, "lesson": ls, "text": t} for l, ls, t in runs],
    }


# ---------------------------------------------------------------------------
# data model
# ---------------------------------------------------------------------------

@dataclass
class Claim:
    idx: int
    text: str
    numbers: set = field(default_factory=set)
    entities: set = field(default_factory=set)

    # filled in by matching
    status: str = "missing"          # covered | partial | missing
    best_emb: float = 0.0
    best_lex: float = 0.0
    best_lesson: str = ""
    best_unit: str = ""
    lessons_covering: list = field(default_factory=list)
    dropped_numbers: list = field(default_factory=list)
    dropped_entities: list = field(default_factory=list)

    def as_dict(self) -> dict:
        d = asdict(self)
        d["numbers"] = sorted(self.numbers)
        d["entities"] = sorted(self.entities)
        return d


@dataclass
class Unit:
    lesson: str
    idx: int
    text: str
    scaffold: bool = False
    best_claim: int = -1
    best_emb: float = 0.0
    ungrounded_numbers: list = field(default_factory=list)
    ungrounded_entities: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# stage 1 — source text from the PDF
# ---------------------------------------------------------------------------

OCR_PSMS = (4, 6, 11, 3)        # column / uniform block / sparse / fully automatic
OCR_RENDER_DPI = 400


@dataclass
class OcrLine:
    key: tuple                   # (page, block, par, line) within its own run
    text: str
    conf: float                  # mean tesseract word confidence, 0-100
    run: str                     # which variant produced it


def _preprocess(png: Path) -> Path:
    """Deskew + locally threshold a scanned page.

    A faded carbon typescript defeats tesseract's global binarisation: the light
    strokes fall below the threshold and vanish. A Sauvola-style local threshold
    keeps them because it compares each pixel to its own neighbourhood instead of
    to the page as a whole. Both this and the untouched render are fed to the vote,
    because preprocessing helps some pages and hurts others.
    """
    out = png.with_name(png.stem + "__prep.png")
    if out.exists():
        return out
    try:
        import numpy as np
        from PIL import Image, ImageOps
        from scipy import ndimage
    except ImportError:
        return png

    img = ImageOps.grayscale(Image.open(png))
    arr = np.asarray(img, dtype=np.float32)

    # --- deskew: the rotation whose horizontal projection has the sharpest peaks
    small = arr[::4, ::4]
    ink = 255.0 - small
    ink -= ink.min()
    if ink.max() > 0:
        ink /= ink.max()
    best_angle, best_score = 0.0, -1.0
    for angle in np.arange(-2.0, 2.01, 0.25):
        rot = ndimage.rotate(ink, angle, reshape=False, order=1, mode="constant", cval=0.0)
        proj = rot.sum(axis=1)
        score = float((np.diff(proj) ** 2).sum())
        if score > best_score:
            best_score, best_angle = score, float(angle)
    if abs(best_angle) >= 0.25:
        arr = ndimage.rotate(arr, best_angle, reshape=False, order=1,
                             mode="constant", cval=255.0)

    # --- Sauvola local threshold
    win, k, R = 41, 0.25, 128.0
    mean = ndimage.uniform_filter(arr, win)
    mean_sq = ndimage.uniform_filter(arr * arr, win)
    std = np.sqrt(np.maximum(mean_sq - mean * mean, 0.0))
    thresh = mean * (1.0 + k * (std / R - 1.0))
    binary = np.where(arr > thresh, 255, 0).astype(np.uint8)

    # --- drop single-pixel speckle without eating thin strokes
    binary = ndimage.median_filter(binary, size=3)

    Image.fromarray(binary).save(out)
    return out


def _tesseract_lines(img: Path, psm: int, run_label: str, page: int) -> list[OcrLine]:
    """One tesseract pass, returned as lines with mean word confidence."""
    proc = subprocess.run(
        ["tesseract", str(img), "stdout", "--psm", str(psm), "-l", "eng", "tsv"],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        return []

    buckets: dict[tuple, list[tuple[str, float]]] = {}
    for row in proc.stdout.splitlines()[1:]:
        cols = row.split("\t")
        if len(cols) < 12:
            continue
        try:
            level = int(cols[0])
            block, par, line = int(cols[2]), int(cols[3]), int(cols[4])
            conf = float(cols[10])
        except ValueError:
            continue
        if level != 5:                     # 5 = word
            continue
        word = cols[11].strip()
        if not word or conf < 0:
            continue
        buckets.setdefault((page, block, par, line), []).append((word, conf))

    lines = []
    for key, words in sorted(buckets.items()):
        text = " ".join(w for w, _ in words).strip()
        if not text:
            continue
        conf = sum(c for _, c in words) / len(words)
        lines.append(OcrLine(key=key, text=text, conf=conf, run=run_label))
    return lines


def _norm_line(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def _vote(runs: list[list[OcrLine]]) -> tuple[list[OcrLine], float]:
    """Merge several OCR passes by per-line majority, breaking ties on confidence.

    Different PSM modes segment the page differently, so lines can't be matched by
    index. The highest-confidence run becomes the spine; every other run contributes
    its best textual match for each spine line. Where two runs agree on a reading we
    take it even if a third run was more confident — agreement across independent
    segmentations is stronger evidence than one pass's self-reported certainty.
    """
    runs = [r for r in runs if r]
    if not runs:
        return [], 0.0

    def mean_conf(r: list[OcrLine]) -> float:
        return sum(l.conf for l in r) / len(r)

    runs.sort(key=mean_conf, reverse=True)
    spine, others = runs[0], runs[1:]

    merged: list[OcrLine] = []
    for line in spine:
        candidates = [line]
        for other in others:
            best, best_ratio = None, 0.0
            for cand in other:
                ratio = SequenceMatcher(None, _norm_line(line.text),
                                        _norm_line(cand.text)).ratio()
                if ratio > best_ratio:
                    best, best_ratio = cand, ratio
            if best is not None and best_ratio >= 0.60:
                candidates.append(best)

        tally: dict[str, list[OcrLine]] = {}
        for c in candidates:
            tally.setdefault(_norm_line(c.text), []).append(c)

        winner_group = max(
            tally.values(),
            key=lambda g: (len(g), max(c.conf for c in g)),
        )
        winner = max(winner_group, key=lambda c: c.conf)
        # confidence reflects agreement as well as tesseract's own score
        agreement_bonus = (len(winner_group) - 1) / max(len(candidates) - 1, 1) * 10.0
        merged.append(OcrLine(key=line.key, text=winner.text,
                              conf=min(100.0, winner.conf + agreement_bonus),
                              run=f"{winner.run} x{len(winner_group)}"))

    conf = sum(l.conf for l in merged) / len(merged) if merged else 0.0
    return merged, conf


def ocr_pdf(pdf: Path, force: bool) -> tuple[str, float, list[OcrLine]]:
    """Multi-pass OCR. Returns (text, mean confidence 0-100, per-line detail)."""
    cache = WORK_DIR / "ocr.json"
    if cache.exists() and not force:
        d = json.loads(cache.read_text(encoding="utf-8"))
        lines = [OcrLine(tuple(l["key"]), l["text"], l["conf"], l["run"]) for l in d["lines"]]
        return d["text"], d["confidence"], lines

    if not shutil.which("pdftoppm") or not shutil.which("tesseract"):
        raise SystemExit("need poppler-utils (pdftoppm) and tesseract on PATH")

    # An embedded text layer beats any amount of OCR — use it when the PDF has one.
    if shutil.which("pdftotext"):
        embedded = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            capture_output=True, text=True, check=False,
        ).stdout
        if len(embedded.strip()) > 200:
            lines = [OcrLine((0, 0, 0, i), t.strip(), 100.0, "pdf-text-layer")
                     for i, t in enumerate(embedded.splitlines()) if t.strip()]
            cache.write_text(json.dumps(
                {"text": embedded, "confidence": 100.0,
                 "lines": [{"key": list(l.key), "text": l.text, "conf": l.conf, "run": l.run}
                           for l in lines]}, indent=2), encoding="utf-8")
            return embedded, 100.0, lines

    render_dir = WORK_DIR / "pages"
    render_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-r", str(OCR_RENDER_DPI), "-gray", "-png",
         str(pdf), str(render_dir / "pg")],
        check=True,
    )

    all_lines: list[OcrLine] = []
    for page_no, png in enumerate(sorted(render_dir.glob("pg-[0-9]*.png"))):
        prepped = _preprocess(png)
        runs = []
        for img, label in ((png, "raw"), (prepped, "prep")):
            for psm in OCR_PSMS:
                runs.append(_tesseract_lines(img, psm, f"{label}/psm{psm}", page_no))
        merged, _ = _vote(runs)
        all_lines.extend(merged)

    text = "\n".join(l.text for l in all_lines)
    conf = sum(l.conf for l in all_lines) / len(all_lines) if all_lines else 0.0
    cache.write_text(json.dumps(
        {"text": text, "confidence": conf,
         "lines": [{"key": list(l.key), "text": l.text, "conf": l.conf, "run": l.run}
                   for l in all_lines]}, indent=2), encoding="utf-8")
    return text, conf, all_lines


def load_source(force_ocr: bool) -> tuple[str, str, float, list[OcrLine]]:
    """Returns (source text, provenance label, OCR confidence 0-100, line detail)."""
    if SIDECAR_SOURCE and SIDECAR_SOURCE.exists():
        clean = normalize_source(SIDECAR_SOURCE.read_text(encoding="utf-8"))
        return clean, f"corrected transcription supplied via --source-text ({SIDECAR_SOURCE.name})", 100.0, []

    pdf = INPUT_PDF
    if not pdf.exists():
        raise SystemExit(f"missing {pdf}")

    raw, conf, lines = ocr_pdf(pdf, force_ocr)
    provenance = (f"{len(OCR_PSMS)}-mode tesseract OCR of {pdf.name}, raw + deskewed/thresholded, "
                  f"per-line majority vote (mean confidence {conf:.1f}%)")
    return normalize_source(raw), provenance, conf, lines


def split_claims(source: str) -> list[Claim]:
    """Break the source into atomic, independently-checkable statements."""
    claims: list[Claim] = []
    for sent in split_sentences(source):
        # a 1940 letter runs clauses together with ';' and ' - ' and ' --- '
        for piece in re.split(r"\s*(?:;|\s-{2,}\s|(?<=\w)\s-\s(?=\w))\s*", sent):
            piece = piece.strip(" -—")
            if not piece:
                continue
            # very long clauses split once more on ', and ' / ', but '
            subs = [piece]
            if len(piece) > 170:
                subs = re.split(r",\s+(?=(?:and|but|so|which|for)\s)", piece)
            for sub in subs:
                sub = sub.strip()
                if len(tokens(sub)) < 2:
                    # keep short-but-factual bits (dates, addresses, amounts)
                    if not re.search(r"\d", sub):
                        continue
                claims.append(
                    Claim(
                        idx=len(claims),
                        text=sub,
                        numbers=numbers_in(sub),
                        entities=entities_in(sub, is_source=True),
                    )
                )
    return claims


# ---------------------------------------------------------------------------
# stage 2 — transcripts from the audio
# ---------------------------------------------------------------------------

AUDIO_EXTS = (".mp3", ".wav", ".m4a", ".flac", ".ogg", ".opus", ".webm", ".aac")


def env_flag(name: str, default: bool) -> bool:
    raw = os.getenv(name, "").strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on"}


def cuda_devices() -> int:
    """How many CUDA devices CTranslate2 can actually use.

    This is the number that matters — a GPU that `nvidia-smi` lists but whose CUDA
    runtime CTranslate2 can't load reports 0 here, which is exactly the case we want
    to fall back on rather than crash inside the first transcribe call.
    """
    try:
        import ctranslate2
        return int(ctranslate2.get_cuda_device_count())
    except Exception:                                          # noqa: BLE001
        return 0


def supported_compute_types(device: str) -> set[str]:
    try:
        import ctranslate2
        return set(ctranslate2.get_supported_compute_types(device))
    except Exception:                                          # noqa: BLE001
        return set()


def resolve_device(requested: str, requested_compute: str | None) -> tuple[str, str, str]:
    """Decide (device, compute_type, reason). `requested` is auto|cuda|cpu."""
    n = cuda_devices()

    if requested == "cpu":
        device = "cpu"
        reason = "forced by --device/WHISPER_DEVICE"
    elif requested == "cuda":
        device = "cuda"
        reason = ("forced by --device/WHISPER_DEVICE"
                  + ("" if n else " — WARNING: CTranslate2 reports 0 CUDA devices"))
    else:
        device = "cuda" if n else "cpu"
        reason = (f"auto: CTranslate2 sees {n} CUDA device(s)" if n
                  else "auto: no CUDA device visible to CTranslate2")

    if requested_compute:
        return device, requested_compute, reason

    if device == "cuda":
        avail = supported_compute_types("cuda")
        for candidate in ("float16", "int8_float16", "bfloat16", "float32"):
            if candidate in avail or not avail:
                return device, candidate, reason
        return device, "float32", reason

    avail = supported_compute_types("cpu")
    return device, ("int8" if not avail or "int8" in avail else "float32"), reason


class Transcriber:
    """faster-whisper wrapper that prefers GPU and degrades to CPU instead of dying."""

    def __init__(self, model_name: str, device: str, compute_type: str,
                 beam_size: int, vad_filter: bool, language: str | None):
        self.model_name = model_name
        self.device = device
        self.compute_type = compute_type
        self.beam_size = beam_size
        self.vad_filter = vad_filter
        self.language = language
        self._model = None

    def _kwargs(self) -> dict:
        kw: dict = {"device": self.device, "compute_type": self.compute_type}
        threads = os.getenv("WHISPER_CPU_THREADS", "").strip()
        workers = os.getenv("WHISPER_NUM_WORKERS", "").strip()
        if self.device == "cpu" and threads.isdigit():
            kw["cpu_threads"] = max(1, int(threads))
        if workers.isdigit():
            kw["num_workers"] = max(1, int(workers))
        return kw

    def model(self):
        if self._model is not None:
            return self._model
        try:
            from faster_whisper import WhisperModel
        except ImportError as exc:
            raise SystemExit(
                "faster_whisper is not importable by this interpreter.\n"
                "Run the script with the venv that already has it:\n"
                "  /home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py"
            ) from exc

        print(f"  loading whisper '{self.model_name}' on {self.device}/{self.compute_type} ...",
              file=sys.stderr)
        try:
            self._model = WhisperModel(self.model_name, **self._kwargs())
        except Exception as exc:                               # noqa: BLE001
            if self.device != "cuda":
                raise
            print(f"  CUDA load failed ({exc}); falling back to CPU/int8", file=sys.stderr)
            self.device, self.compute_type = "cpu", "int8"
            self._model = WhisperModel(self.model_name, **self._kwargs())
        return self._model

    def run(self, path: Path) -> dict:
        segments, info = self.model().transcribe(
            str(path),
            beam_size=max(1, self.beam_size),
            vad_filter=self.vad_filter,
            language=self.language,
        )
        segs = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
        return {
            "file": path.name,
            "duration": float(getattr(info, "duration", 0.0) or 0.0),
            "device": self.device,
            "compute_type": self.compute_type,
            "model": self.model_name,
            "vad_filter": self.vad_filter,
            "beam_size": self.beam_size,
            "segments": segs,
            "text": " ".join(s["text"] for s in segs).strip(),
        }


def audio_files() -> list[Path]:
    files = sorted(p for p in AUDIO_DIR.iterdir()
                   if p.is_file() and p.suffix.lower() in AUDIO_EXTS)
    if not files:
        raise SystemExit(f"no audio files in {AUDIO_DIR} (looked for {', '.join(AUDIO_EXTS)})")
    return files


def load_lessons(tr: Transcriber, force: bool) -> tuple[list[tuple[str, str]], dict[str, float]]:
    cache_dir = WORK_DIR / "transcripts"
    cache_dir.mkdir(parents=True, exist_ok=True)

    lessons: list[tuple[str, str]] = []
    durations: dict[str, float] = {}

    for path in audio_files():
        cache = cache_dir / (path.stem + ".json")
        if cache.exists() and not force:
            data = json.loads(cache.read_text(encoding="utf-8"))
            print(f"  cached  {path.name}", file=sys.stderr)
        else:
            print(f"  transcribing {path.name} ...", file=sys.stderr)
            data = tr.run(path)
            cache.write_text(json.dumps(data, indent=2), encoding="utf-8")
        if not data.get("text"):
            print(f"  WARNING: empty transcript for {path.name}", file=sys.stderr)
        lessons.append((path.stem, data["text"]))
        durations[path.stem] = data.get("duration") or probe_duration(path)

    return lessons, durations


def probe_duration(path: Path) -> float:
    """Fallback duration when Whisper didn't report one. ffprobe is optional."""
    if not shutil.which("ffprobe"):
        return 0.0
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=False,
    )
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


# ---------------------------------------------------------------------------
# stage 3 — matching
# ---------------------------------------------------------------------------

def build_units(lessons: list[tuple[str, str]]) -> list[Unit]:
    units: list[Unit] = []
    for name, text in lessons:
        for i, sent in enumerate(split_sentences(text)):
            units.append(Unit(lesson=name, idx=i, text=sent, scaffold=is_scaffold(sent)))
    return units


EMBED_MODEL_NAME = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
_EMBEDDER = None


def torch_device() -> str:
    """Torch CUDA availability is independent of CTranslate2's — probe it separately.

    A CPU-only torch build sits happily alongside a GPU-capable CTranslate2, so the
    embedding step can end up on CPU while transcription runs on GPU. That is fine:
    embedding a few hundred short sentences is not the expensive half of this job.
    """
    if os.getenv("EMBED_DEVICE", "").strip():
        return os.getenv("EMBED_DEVICE").strip()
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except Exception:                                          # noqa: BLE001
        return "cpu"


def embedder():
    global _EMBEDDER
    if _EMBEDDER is not None:
        return _EMBEDDER
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise SystemExit(
            "sentence_transformers is not importable by this interpreter.\n"
            "Run the script with the venv that already has it:\n"
            "  /home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py"
        ) from exc
    dev = torch_device()
    try:
        _EMBEDDER = SentenceTransformer(EMBED_MODEL_NAME, device=dev)
    except Exception as exc:                                   # noqa: BLE001
        if dev == "cpu":
            raise
        print(f"  embedder CUDA init failed ({exc}); using CPU", file=sys.stderr)
        _EMBEDDER = SentenceTransformer(EMBED_MODEL_NAME, device="cpu")
    return _EMBEDDER


def embed(texts: list[str]):
    return embedder().encode(texts, normalize_embeddings=True, show_progress_bar=False)


def match(claims: list[Claim], units: list[Unit]):
    import numpy as np

    # compare each claim against single sentences AND adjacent pairs, since a claim
    # is often explained across two narrated sentences
    windows: list[tuple[str, str]] = []      # (lesson, text)
    for i, u in enumerate(units):
        windows.append((u.lesson, u.text))
        if i + 1 < len(units) and units[i + 1].lesson == u.lesson:
            windows.append((u.lesson, u.text + " " + units[i + 1].text))

    claim_vecs = embed([c.text for c in claims])
    win_vecs = embed([w[1] for w in windows])
    unit_vecs = win_vecs[: 0]  # placeholder, recomputed below for unit-level use

    sims = np.asarray(claim_vecs) @ np.asarray(win_vecs).T   # (claims x windows)

    win_tokens = [tokens(w[1]) for w in windows]
    win_numbers = [numbers_in(w[1]) for w in windows]
    win_entities = [entities_in(w[1], is_source=False) for w in windows]

    # raw text per side, for the case-insensitive fallback both directions need
    lesson_text: dict[str, str] = {}
    for u in units:
        lesson_text[u.lesson] = lesson_text.get(u.lesson, "") + " " + u.text
    source_text = " ".join(c.text for c in claims)

    for ci, claim in enumerate(claims):
        ctok = tokens(claim.text)
        lex = [token_f1(ctok, wt) for wt in win_tokens]

        best_i = int(np.argmax(sims[ci]))
        best_emb = float(sims[ci][best_i])
        best_lex_i = int(max(range(len(lex)), key=lambda k: lex[k])) if lex else 0
        best_lex = lex[best_lex_i] if lex else 0.0

        # whichever signal is stronger picks the exemplar
        pick = best_i if best_emb / max(COVERED_EMB, 1e-6) >= best_lex / max(COVERED_LEX, 1e-6) else best_lex_i

        claim.best_emb = best_emb
        claim.best_lex = best_lex
        claim.best_lesson = windows[pick][0]
        claim.best_unit = windows[pick][1]

        if best_emb >= COVERED_EMB or best_lex >= COVERED_LEX:
            claim.status = "covered"
        elif best_emb >= PARTIAL_EMB or best_lex >= PARTIAL_LEX:
            claim.status = "partial"
        else:
            claim.status = "missing"

        # a claim only truly survives if its hard facts survive with it
        if claim.status == "covered":
            missing_nums = [n for n in claim.numbers if n not in win_numbers[pick]]
            missing_ents = [e for e in claim.entities
                            if not entity_matches(e, win_entities[pick])]
            # allow the fact to appear anywhere in the same lesson
            same_lesson = [k for k, w in enumerate(windows) if w[0] == windows[pick][0]]
            missing_nums = [n for n in missing_nums
                            if not any(n in win_numbers[k] for k in same_lesson)]
            missing_ents = [e for e in missing_ents
                            if not any(entity_matches(e, win_entities[k]) for k in same_lesson)]
            # last chance: the lesson may say the name in lower case (see spoken_in)
            missing_ents = [e for e in missing_ents
                            if not spoken_in(e, lesson_text[windows[pick][0]])]
            if missing_nums or missing_ents:
                claim.status = "partial"
                claim.dropped_numbers = sorted(missing_nums)
                claim.dropped_entities = sorted(missing_ents)

        # which lessons touch this claim at all — the redundancy signal
        lessons_hit = set()
        for wi, (lesson, _) in enumerate(windows):
            if sims[ci][wi] >= COVERED_EMB or lex[wi] >= COVERED_LEX:
                lessons_hit.add(lesson)
        claim.lessons_covering = sorted(lessons_hit)

    # reverse direction: which narrated sentences have no source at all
    unit_vecs = embed([u.text for u in units])
    rsims = np.asarray(unit_vecs) @ np.asarray(claim_vecs).T   # (units x claims)
    claim_numbers = set().union(*[c.numbers for c in claims]) if claims else set()
    claim_entities = set().union(*[c.entities for c in claims]) if claims else set()

    for ui, unit in enumerate(units):
        bi = int(np.argmax(rsims[ui]))
        unit.best_claim = bi
        unit.best_emb = float(rsims[ui][bi])
        unit.ungrounded_numbers = sorted(n for n in numbers_in(unit.text)
                                         if n not in claim_numbers)
        unit.ungrounded_entities = sorted(
            e for e in entities_in(unit.text, is_source=False)
            if not entity_matches(e, claim_entities) and not spoken_in(e, source_text)
        )

    return units


def near_duplicates(units: list[Unit]) -> list[tuple[Unit, Unit, float]]:
    import numpy as np

    substantive = [u for u in units if not u.scaffold and len(tokens(u.text)) >= 4]
    if len(substantive) < 2:
        return []
    vecs = np.asarray(embed([u.text for u in substantive]))
    sims = vecs @ vecs.T
    pairs = []
    for i in range(len(substantive)):
        for j in range(i + 1, len(substantive)):
            if sims[i][j] >= NEAR_DUP_EMB:
                pairs.append((substantive[i], substantive[j], float(sims[i][j])))
    pairs.sort(key=lambda p: -p[2])
    return pairs


# ---------------------------------------------------------------------------
# stage 4 — Claude adjudication (optional)
# ---------------------------------------------------------------------------

ADJUDICATION_SCHEMA = {
    "type": "object",
    "properties": {
        "coverage_verdict": {"type": "string"},
        "coverage_percent": {"type": "integer"},
        "missing_from_course": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "source_fact": {"type": "string"},
                    "why_it_matters": {"type": "string"},
                },
                "required": ["source_fact", "why_it_matters"],
                "additionalProperties": False,
            },
        },
        "fabrications": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim_in_audio": {"type": "string"},
                    "lesson": {"type": "string"},
                    "kind": {
                        "type": "string",
                        "enum": ["invented_fact", "outside_knowledge", "misreading",
                                 "unsupported_inference", "likely_transcription_artifact"],
                    },
                    "explanation": {"type": "string"},
                },
                "required": ["claim_in_audio", "lesson", "kind", "explanation"],
                "additionalProperties": False,
            },
        },
        "redundancy": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "repeated_content": {"type": "string"},
                    "lessons": {"type": "string"},
                    "justified": {"type": "boolean"},
                    "note": {"type": "string"},
                },
                "required": ["repeated_content", "lessons", "justified", "note"],
                "additionalProperties": False,
            },
        },
        "teachability": {
            "type": "object",
            "properties": {
                "verdict": {"type": "string"},
                "strengths": {"type": "array", "items": {"type": "string"}},
                "weaknesses": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["verdict", "strengths", "weaknesses"],
            "additionalProperties": False,
        },
        "originality": {
            "type": "object",
            "properties": {
                "verdict": {"type": "string",
                            "enum": ["taught", "mixed", "largely recited"]},
                "note": {"type": "string"},
            },
            "required": ["verdict", "note"],
            "additionalProperties": False,
        },
        "bottom_line": {"type": "string"},
    },
    "required": ["coverage_verdict", "coverage_percent", "missing_from_course",
                 "fabrications", "originality", "redundancy", "teachability",
                 "bottom_line"],
    "additionalProperties": False,
}

ADJUDICATION_PROMPT = """\
You are auditing an AI-generated audio course against its single source document.

The source is reproduced verbatim below — read what kind of document it actually is
rather than assuming a form. The course is {n} narrated lessons. The lesson text
below is a speech-to-text transcript of the delivered audio, so misspelled proper
nouns and odd word choices may be transcription artifacts rather than authoring
errors — label those `likely_transcription_artifact` rather than `invented_fact`
when the surrounding sentence clearly tracks the source.

The standard is teaching equivalence: would someone who only listened come away
knowing what someone who read the document knows? Judge the *content*. Attribution,
authorship, title and copyright are explicitly out of scope — do not report them as
gaps, and do not count them toward or against coverage.

Anything asserted in the audio that the source does not support is still a finding,
including outside knowledge presented as though it came from the source.

Weigh the medium honestly. Where the source teaches through an image, diagram or
table, a listener has no picture; narration that recites a caption without explaining
it transfers nothing, however faithful it is to the words. That is a teaching failure
even though it scores as covered.

<source_document>
{source}
</source_document>

<course_lessons>
{lessons}
</course_lessons>

<mechanical_analysis>
A deterministic pass (sentence embeddings + entity/number grounding) produced these
signals. Treat them as leads to verify, not conclusions:

{signals}
</mechanical_analysis>

Answer five questions:
1. Would a listener finish knowing what a reader knows? Give `coverage_percent` as
   your own judgement of the share of the source's teachable content that actually
   transfers through audio (not a token count, and not counting front matter).
2. Did the course invent, import, or misread anything?
3. Is the course teaching the material or reciting it? The mechanical pass reports
   what share of narration is copied word-for-word and quotes the longest runs. Set
   `originality.verdict` to one of `taught`, `mixed`, or `largely recited`, and say in
   `note` what the course does in its own words versus what it lifts. Discount runs
   that are scripture or another quoted third text — the source quoting a verse and
   the course quoting the same verse is not the course copying the source.
4. What is repeated across lessons, and is the repetition pedagogically justified or
   just padding?
5. Is the surviving content arranged so a listener actually learns it?

Be specific and quote the audio. Do not pad the lists — only real findings.
"""


def adjudicate(source: str, lessons: list[tuple[str, str]], signals: str) -> dict | None:
    try:
        import anthropic
    except ImportError:
        print("  anthropic SDK not installed — skipping Claude pass", file=sys.stderr)
        return None

    try:
        client = anthropic.Anthropic()
    except Exception as exc:                                  # noqa: BLE001
        print(f"  no Anthropic credentials — skipping Claude pass ({exc})", file=sys.stderr)
        return None

    lesson_block = "\n\n".join(
        f"<lesson name=\"{name}\">\n{text}\n</lesson>" for name, text in lessons
    )
    prompt = ADJUDICATION_PROMPT.format(
        n=len(lessons), source=source, lessons=lesson_block, signals=signals
    )

    try:
        with client.messages.stream(
            model="claude-opus-5",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            output_config={
                "effort": "high",
                "format": {"type": "json_schema", "schema": ADJUDICATION_SCHEMA},
            },
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            message = stream.get_final_message()
    except Exception as exc:                                  # noqa: BLE001
        print(f"  Claude pass failed: {exc}", file=sys.stderr)
        return None

    if message.stop_reason == "refusal":
        print("  Claude declined the request — skipping adjudication", file=sys.stderr)
        return None

    text = next((b.text for b in message.content if b.type == "text"), "")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("  Claude returned unparseable JSON — skipping adjudication", file=sys.stderr)
        return None


def signal_digest(claims: list[Claim], units: list[Unit], dups,
                  lifted: dict | None = None) -> str:
    lines = []
    if lifted:
        lines.append(
            f"- verbatim overlap: {lifted['percent']:.1f}% of narrated words sit inside "
            f"a run of {lifted['shingle']}+ consecutive words copied from the source "
            f"({len(lifted['runs'])} runs). Longest runs:")
        for r in lifted["runs"][:12]:
            lines.append(f'    * [{r["length"]} words, {r["lesson"]}] "{r["text"][:220]}"')
    miss = [c for c in claims if c.status == "missing"]
    part = [c for c in claims if c.status == "partial"]
    lines.append(f"- {len(claims)} source claims: "
                 f"{sum(1 for c in claims if c.status == 'covered')} covered, "
                 f"{len(part)} partial, {len(miss)} missing")
    if miss:
        lines.append("- flagged missing:")
        for c in miss[:25]:
            lines.append(f'    * "{c.text}"  (best sim {c.best_emb:.2f})')
    if part:
        lines.append("- flagged partial / detail dropped:")
        for c in part[:25]:
            detail = ""
            if c.dropped_numbers or c.dropped_entities:
                detail = f"  [dropped: {', '.join(c.dropped_numbers + c.dropped_entities)}]"
            lines.append(f'    * "{c.text}"{detail}')
    ung = [u for u in units if not u.scaffold and u.best_emb < UNGROUNDED_EMB]
    if ung:
        lines.append("- audio sentences with no close source match:")
        for u in ung[:25]:
            lines.append(f'    * [{u.lesson}] "{u.text}" (sim {u.best_emb:.2f})')
    ent = [u for u in units if u.ungrounded_entities or u.ungrounded_numbers]
    if ent:
        lines.append("- names/numbers in audio not found in source:")
        for u in ent[:25]:
            bits = u.ungrounded_entities + u.ungrounded_numbers
            lines.append(f'    * [{u.lesson}] {", ".join(bits)} — "{u.text}"')
    if dups:
        lines.append("- near-duplicate statements across lessons:")
        for a, b, s in dups[:20]:
            lines.append(f'    * {s:.2f}  [{a.lesson}] "{a.text}"  ||  [{b.lesson}] "{b.text}"')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# stage 5 — report
# ---------------------------------------------------------------------------

def pct(n: int, d: int) -> float:
    return (100.0 * n / d) if d else 0.0


def render_ocr_refusal(source: str, provenance: str, conf: float, gate: float,
                       lex: float, lex_gate: float, offenders: list[str],
                       lines: list[OcrLine], lessons: list[tuple[str, str]],
                       durations: dict[str, float], tr: "Transcriber") -> str:
    """The source text is too damaged to score against. Say so, and help fix it."""
    L = []
    A = L.append
    A("# Audit halted — source text is not reliable enough to score")
    A("")
    A("| Signal | Result | Gate | |")
    A("| --- | --- | --- | --- |")
    A(f"| Dictionary validity of OCR | {lex:.1f}% | {lex_gate:.0f}% | "
      f"{'**FAIL**' if lex < lex_gate else 'pass'} |")
    A(f"| Mean tesseract word confidence | {conf:.1f}% | {gate:.0f}% | "
      f"{'**FAIL**' if conf < gate else 'pass'} |")
    A("")
    A("Coverage percentages are deliberately withheld. Scoring a course against a "
      "mangled source does not measure the course — it measures the OCR. Words the "
      "scanner lost would be reported as content the course dropped, and the "
      "resulting number would look authoritative while being meaningless.")
    A("")
    if conf >= gate and lex < lex_gate:
        A("Note that tesseract's own confidence **passed** while dictionary validity "
          "failed. Tesseract can be confidently wrong on a faded typescript, which is "
          "why both signals are checked.")
        A("")
    if offenders:
        A(f"### {len(offenders)} words the OCR produced that are not real words")
        A("")
        A("These are where the damage is. Fix these and the text is usable; a handful "
          "may be legitimate (foreign words, archaic spellings, the writer's own typos).")
        A("")
        A("> " + "  ·  ".join(f"`{w}`" for w in offenders))
        A("")
    A(f"- **Source:** `{INPUT_PDF}` — {provenance}")
    A(f"- **Audio:** {len(lessons)} file(s), {sum(durations.values())/60:.1f} min "
      f"(transcribed on `{tr.device}/{tr.compute_type}`; transcripts are cached and "
      f"will not be recomputed)")
    A("")
    A("## Fix it")
    A("")
    A("1. Read the OCR below against the scan and correct it.")
    A("2. Save the corrected text to a file, e.g. `source_corrected.txt`.")
    A("3. Re-run pointing at it — the audio transcripts are already cached, so this "
      "is fast:")
    A("")
    A("```")
    A("/home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py \\")
    A("    --source-text source_corrected.txt")
    A("```")
    A("")
    A(f"To publish numbers from the OCR anyway, re-run with `--ignore-ocr-gate` "
      f"(or lower the bars with `--ocr-gate {max(0, int(conf) - 5)} "
      f"--lex-gate {max(0, int(lex) - 5)}`). The report will carry the caveat.")
    A("")
    A("## OCR output, lowest-confidence lines first")
    A("")
    if lines:
        A("| Conf | Winning pass | Line |")
        A("| --- | --- | --- |")
        for l in sorted(lines, key=lambda l: l.conf):
            A(f"| {l.conf:.0f}% | `{l.run}` | {l.text} |")
        A("")
    A("## OCR output, in reading order")
    A("")
    A("```")
    A(source)
    A("```")
    A("")
    A("_Generated by `analyze_course.py`._")
    return "\n".join(L)


def render(source: str, provenance: str, ocr_conf: float, gate: float,
           ocr_lex: float, lex_gate: float, gate_bypassed: bool,
           claims: list[Claim], units: list[Unit], lessons: list[tuple[str, str]],
           dups, durations: dict[str, float], verdict: dict | None,
           tr: "Transcriber", lifted: dict,
           front_matter: list[Claim]) -> str:

    covered = [c for c in claims if c.status == "covered"]
    partial = [c for c in claims if c.status == "partial"]
    missing = [c for c in claims if c.status == "missing"]

    src_words = len(re.findall(r"\w+", source))
    out_words = sum(len(re.findall(r"\w+", t)) for _, t in lessons)
    total_secs = sum(durations.values())

    substantive = [u for u in units if not u.scaffold]
    scaffold_n = len(units) - len(substantive)
    ungrounded = [u for u in substantive if u.best_emb < UNGROUNDED_EMB]
    ent_flags = [u for u in units if u.ungrounded_entities or u.ungrounded_numbers]

    L = []
    A = L.append

    A("# Audio course vs. source document — audit report")
    A("")
    A(f"- **Source:** `{INPUT_PDF.name}` — {provenance}")
    A(f"- **Course:** {len(lessons)} lessons, {total_secs/60:.1f} min of audio")
    A(f"- **Audio transcribed with:** faster-whisper `{tr.model_name}` on "
      f"`{tr.device}/{tr.compute_type}` (beam {tr.beam_size}, VAD {'on' if tr.vad_filter else 'off'}). "
      f"Wording below is the transcript, not the authoring text — some oddities are "
      f"speech-recognition artifacts, and are labelled as such where identifiable.")
    A("")

    if gate_bypassed:
        A(f"> ⚠️ **Numbers below are unreliable.** The source text failed a quality "
          f"gate ({ocr_conf:.1f}% OCR confidence vs {gate:.0f}%; "
          f"{ocr_lex:.1f}% dictionary validity vs {lex_gate:.0f}%) and this "
          f"run was forced through with `--ignore-ocr-gate`. Words the scanner lost "
          f"are indistinguishable here from content the course dropped, so treat every "
          f"\"missing\" row as a lead to check by eye rather than a finding. Re-run "
          f"with `--source-text` against a corrected transcription for figures worth "
          f"quoting.")
        A("")

    # ---- headline
    A("## 1. Headline numbers")
    A("")
    A("| Measure | Value |")
    A("| --- | --- |")
    A(f"| Source statements identified | {len(claims)} |")
    A(f"| Fully carried into the audio | {len(covered)} ({pct(len(covered), len(claims)):.0f}%) |")
    A(f"| Carried but with detail dropped | {len(partial)} ({pct(len(partial), len(claims)):.0f}%) |")
    A(f"| Absent from the audio | {len(missing)} ({pct(len(missing), len(claims)):.0f}%) |")
    A(f"| **Content coverage (full + partial)** | **{pct(len(covered)+len(partial), len(claims)):.0f}%** |")
    A(f"| Source length | {src_words} words |")
    A(f"| Course length | {out_words} words |")
    A(f"| Expansion ratio | {out_words/max(src_words,1):.1f}x |")
    A(f"| Narrated sentences | {len(units)} ({scaffold_n} teaching scaffold, {len(substantive)} content) |")
    A(f"| Content sentences with no close source match | {len(ungrounded)} |")
    A(f"| Sentences naming something absent from the source | {len(ent_flags)} |")
    A(f"| Near-duplicate statement pairs across lessons | {len(dups)} |")
    A(f"| **Narration lifted word-for-word from the source** | "
      f"**{lifted['percent']:.0f}%** |")
    A("")
    A("Read the last two rows together. Coverage should be high and lifted should be "
      "low; a course that reads the source aloud scores well on the first *because* it "
      "scores badly on the second. An expansion ratio near 1.0x is the same warning "
      "from the other direction — teaching adds words, copying does not.")
    A("")

    if front_matter:
        A(f"<details><summary>{len(front_matter)} statement(s) excluded as front matter, "
          f"not scored</summary>")
        A("")
        A("Attribution, title and copyright boilerplate. A course that omits these has "
          "not failed the listener, so they are held out of the coverage numbers above. "
          "Score them like any other statement with `--keep-front-matter`.")
        A("")
        for c in front_matter:
            A(f"- `{c.idx:02d}` {c.text[:200]}{'…' if len(c.text) > 200 else ''}")
        A("")
        A("</details>")
        A("")

    if verdict:
        A(f"> **Claude's independent read of coverage: {verdict['coverage_percent']}%** — "
          f"{verdict['coverage_verdict']}")
        A("")
        if verdict.get("originality"):
            o = verdict["originality"]
            A(f"> **Is this taught or recited? {o['verdict']}** — {o['note']}")
            A("")

    # ---- Q1 coverage
    A("## 2. Does the audio carry all the context?")
    A("")
    if missing:
        A(f"**No — {len(missing)} statement(s) from the source never appear in any lesson.**")
        A("")
        A("| # | Missing from the course | Closest thing the audio says |")
        A("| --- | --- | --- |")
        for c in missing:
            closest = c.best_unit[:90] + ("…" if len(c.best_unit) > 90 else "")
            A(f"| {c.idx} | {c.text} | _{closest}_ (sim {c.best_emb:.2f}) |")
        A("")
    else:
        A("**Yes — every statement in the source has a corresponding passage in the audio.**")
        A("")

    if partial:
        A(f"### Carried, but with specifics dropped ({len(partial)})")
        A("")
        A("| Source statement | What went missing | Where it landed |")
        A("| --- | --- | --- |")
        for c in partial:
            drop = ", ".join(f"`{d}`" for d in (c.dropped_numbers + c.dropped_entities)) or "—"
            A(f"| {c.text} | {drop} | {c.best_lesson} |")
        A("")

    # ---- Q2 fabrication
    A("## 3. Did the AI invent anything?")
    A("")
    if ungrounded:
        A(f"### Narrated content with no close match in the source ({len(ungrounded)})")
        A("")
        A("| Lesson | Sentence | Similarity to nearest source statement |")
        A("| --- | --- | --- |")
        for u in ungrounded:
            A(f"| {u.lesson} | {u.text} | {u.best_emb:.2f} |")
        A("")
    else:
        A("No narrated sentence sits far enough from the source to be flagged mechanically.")
        A("")

    if ent_flags:
        A(f"### Names and numbers spoken that are not in the source ({len(ent_flags)})")
        A("")
        A("| Lesson | Not in source | Sentence |")
        A("| --- | --- | --- |")
        for u in ent_flags:
            bits = ", ".join(f"`{b}`" for b in (u.ungrounded_entities + u.ungrounded_numbers))
            A(f"| {u.lesson} | {bits} | {u.text} |")
        A("")
        A("_Fuzzy matching is applied before flagging, so mangled-but-recognisable names "
          "are not listed here. What remains is either genuinely new information or a "
          "transcription error severe enough to change the word._")
        A("")

    if verdict and verdict["fabrications"]:
        A("### Adjudicated findings")
        A("")
        for f in verdict["fabrications"]:
            A(f"- **{f['kind'].replace('_', ' ')}** — _{f['lesson']}_: “{f['claim_in_audio']}”")
            A(f"  {f['explanation']}")
        A("")
    elif verdict:
        A("### Adjudicated findings")
        A("")
        A("No fabrications confirmed on review.")
        A("")

    # ---- Q3b originality
    A("## 4. Is it taught, or is it read out?")
    A("")
    n = lifted["shingle"]
    A(f"**{lifted['percent']:.1f}% of narrated words sit inside a run of {n}+ consecutive "
      f"words copied from the source** ({lifted['lifted']:,} of {lifted['words']:,} words, "
      f"{len(lifted['runs'])} runs).")
    A("")
    A("| Lesson | Words | Lifted | Longest unbroken run |")
    A("| --- | --- | --- | --- |")
    for r in lifted["per_lesson"]:
        A(f"| {r['lesson']} | {r['words']:,} | {r['percent']:.0f}% | "
          f"{r['longest_run']} words |")
    A("")
    if lifted["runs"]:
        A(f"### Longest passages carried over word-for-word")
        A("")
        for r in lifted["runs"][:15]:
            A(f"- **{r['length']} words** — _{r['lesson']}_")
            A(f"  > {r['text'][:400]}{'…' if len(r['text']) > 400 else ''}")
        A("")
    A("_Scripture is the honest exception: where the source quotes a verse and the "
      "course quotes the same verse, the run above is shared quotation of a third text, "
      "not the source's own prose. Check long runs against that before treating them as "
      "copying._")
    A("")

    # ---- Q3 redundancy
    A("## 5. Duplication and redundancy")
    A("")
    multi = [c for c in claims if len(c.lessons_covering) > 1]
    A(f"{len(multi)} of {len(claims)} source statements are taught in more than one lesson "
      f"({pct(len(multi), len(claims)):.0f}%).")
    A("")
    if multi:
        A("| Source statement | Repeated in |")
        A("| --- | --- |")
        for c in sorted(multi, key=lambda c: -len(c.lessons_covering)):
            A(f"| {c.text} | {', '.join(c.lessons_covering)} |")
        A("")
    if dups:
        A(f"### Near-identical narrated sentences ({len(dups)} pairs)")
        A("")
        A("| Sim | A | B |")
        A("| --- | --- | --- |")
        for a, b, s in dups:
            A(f"| {s:.2f} | _{a.lesson}_<br>{a.text} | _{b.lesson}_<br>{b.text} |")
        A("")
    if verdict and verdict["redundancy"]:
        A("### Adjudicated redundancy")
        A("")
        for r in verdict["redundancy"]:
            tag = "justified" if r["justified"] else "**not justified**"
            A(f"- **{r['repeated_content']}** ({r['lessons']}) — {tag}. {r['note']}")
        A("")

    # ---- Q4 teachability
    A("## 6. Is it teachable?")
    A("")
    A("| Lesson | Minutes | Words | Sentences | Scaffold | Source statements touched | Direct quotes |")
    A("| --- | --- | --- | --- | --- | --- | --- |")
    for name, text in lessons:
        lu = [u for u in units if u.lesson == name]
        touched = len({c.idx for c in claims if name in c.lessons_covering})
        quotes = sum(1 for u in lu if re.search(
            r"\b(he (says|writes|states)|the author (says|writes|states)|"
            r"he adds|he even wondered)\b", u.text.lower()))
        words = len(re.findall(r"\w+", text))
        mins = durations.get(name, 0) / 60
        scaf = sum(1 for u in lu if u.scaffold)
        A(f"| {name} | {mins:.1f} | {words} | {len(lu)} | {scaf} | {touched} | {quotes} |")
    A("")
    if verdict:
        t = verdict["teachability"]
        A(f"**Verdict:** {t['verdict']}")
        A("")
        if t["strengths"]:
            A("Strengths:")
            for s in t["strengths"]:
                A(f"- {s}")
            A("")
        if t["weaknesses"]:
            A("Weaknesses:")
            for w in t["weaknesses"]:
                A(f"- {w}")
            A("")

    if verdict and verdict["missing_from_course"]:
        A("## 7. What a listener will never learn")
        A("")
        for m in verdict["missing_from_course"]:
            A(f"- **{m['source_fact']}** — {m['why_it_matters']}")
        A("")

    if verdict:
        A("## Bottom line")
        A("")
        A(verdict["bottom_line"])
        A("")

    A("---")
    A("")
    A("<details><summary>Source statements as parsed</summary>")
    A("")
    for c in claims:
        mark = {"covered": "x", "partial": "~", "missing": " "}[c.status]
        A(f"- [{mark}] `{c.idx:02d}` {c.text}")
    A("")
    A("</details>")
    A("")
    A("_Generated by `analyze_course.py`. Coverage percentages are computed from "
      "sentence-embedding similarity plus entity/number grounding against the parsed "
      "source statements shown above; they are a measurement of this parse, not a "
      "universal truth._")

    return "\n".join(L)


# ---------------------------------------------------------------------------

def preflight(tr: Transcriber, reason: str, gate: float, lex_gate: float) -> int:
    """Print exactly what this box will do, so prod can be validated before a long run."""
    ok = True

    def row(label: str, value: str, good: bool = True) -> None:
        nonlocal ok
        ok = ok and good
        print(f"  {'ok ' if good else 'FAIL'}  {label:<26} {value}")

    print("\nanalyze_course.py preflight\n" + "-" * 62)

    # A supplied --source-text replaces the PDF entirely, so neither the file nor the
    # OCR toolchain is required. Without this, a host that only ever scores against a
    # sidecar transcription fails preflight over tools it will never call.
    need_pdf = SIDECAR_SOURCE is None

    print("\npaths")
    if need_pdf:
        row("source pdf", str(INPUT_PDF), INPUT_PDF.exists())
    else:
        print(f"  --   source pdf                 not needed (--source-text supplied)")
    try:
        n_audio = len(audio_files())
        row("audio dir", f"{AUDIO_DIR}  ({n_audio} file(s))", True)
    except SystemExit as exc:
        row("audio dir", str(exc), False)
    row("work dir", str(WORK_DIR), True)
    row("report out", str(REPORT_MD), True)
    if SIDECAR_SOURCE is None:
        print(f"  --   source text               from PDF via OCR "
              f"(gates: {gate:.0f}% confidence, {lex_gate:.0f}% dictionary; "
              f"override with --source-text FILE)")
        nwords = len(dictionary())
        print(f"  {'ok ' if nwords else '--  '} wordlist                  "
              f"{f'{nwords} words' if nwords else 'none found — dictionary gate DISABLED'}")
    else:
        row("source text", str(SIDECAR_SOURCE), SIDECAR_SOURCE.exists())

    print("\nbinaries")
    for name, required in (("pdftoppm", need_pdf), ("tesseract", need_pdf),
                           ("pdftotext", False), ("ffprobe", False)):
        found = shutil.which(name)
        if required:
            row(name, found or "NOT FOUND", bool(found))
        else:
            print(f"  {'ok ' if found else '--  '} {name:<26} "
                  f"{found or 'not found (optional)'}")

    print("\npython packages")
    for mod, required in (("faster_whisper", True), ("ctranslate2", True),
                          ("sentence_transformers", True), ("numpy", True),
                          ("torch", False), ("anthropic", False)):
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "?")
            if required:
                row(mod, ver, True)
            else:
                print(f"  ok   {mod:<26} {ver}")
        except Exception as exc:                               # noqa: BLE001
            if required:
                row(mod, f"NOT IMPORTABLE ({exc})", False)
            else:
                print(f"  --   {mod:<26} not installed (optional)")

    print("\ncompute")
    n = cuda_devices()
    print(f"  {'ok ' if n else '--  '} ctranslate2 CUDA devices  {n}")
    if n:
        print(f"       cuda compute types     {sorted(supported_compute_types('cuda'))}")
    print(f"       cpu compute types      {sorted(supported_compute_types('cpu'))}")
    print(f"  ->   transcription          {tr.device} / {tr.compute_type}  ({reason})")
    print(f"  ->   whisper model          {tr.model_name}"
          f"   beam={tr.beam_size} vad={tr.vad_filter} lang={tr.language or 'auto'}")
    print(f"  ->   embeddings             {torch_device()}  ({EMBED_MODEL_NAME})")
    if tr.device == "cpu" and n == 0:
        print("\n  note  No GPU visible to CTranslate2 on this box. Transcription will run on\n"
              "        CPU — correct, just slower. On a GPU host this resolves to cuda\n"
              "        automatically; force it with --device cuda to fail loudly instead.")

    print("\ncredentials")
    key = bool(os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN"))
    profile = (Path.home() / ".config" / "anthropic").exists()
    if key or profile:
        print(f"  ok   anthropic                 {'env var' if key else 'ant auth profile'}")
    else:
        print("  --   anthropic                 none — adjudication pass will be skipped\n"
              "                                  (use --no-llm, or --adjudication FILE)")

    print("\n" + "-" * 62)
    print("READY" if ok else "NOT READY — fix the FAIL rows above")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="print resolved device/model/deps and exit without doing work")
    ap.add_argument("--no-llm", action="store_true", help="skip the Claude adjudication pass")
    ap.add_argument("--adjudication", metavar="FILE",
                    help="use a pre-computed adjudication JSON (matching ADJUDICATION_SCHEMA) "
                         "instead of calling the API; useful where no credentials are available")
    ap.add_argument("--force-ocr", action="store_true")
    ap.add_argument("--force-transcribe", action="store_true")

    o = ap.add_argument_group("source text")
    o.add_argument("--ocr-gate", type=float, default=OCR_GATE, metavar="PCT",
                   help=f"minimum mean tesseract word confidence (default {OCR_GATE:.0f}%%)")
    o.add_argument("--lex-gate", type=float, default=LEX_GATE, metavar="PCT",
                   help=f"minimum share of lowercase tokens that are real words "
                        f"(default {LEX_GATE:.0f}%%). This is the signal that actually "
                        f"discriminates; tesseract confidence alone can pass bad text.")
    o.add_argument("--ignore-ocr-gate", action="store_true",
                   help="score anyway when the source text is below either gate; the "
                        "report carries a prominent unreliability warning")
    o.add_argument("--keep-front-matter", action="store_true",
                   help="score copyright/registration/title boilerplate as teaching "
                        "content too (default: excluded and listed separately)")

    v = ap.add_argument_group("originality")
    v.add_argument("--verbatim-shingle", type=int, default=VERBATIM_SHINGLE, metavar="N",
                   help=f"a narrated word counts as lifted when it sits in a run of N+ "
                        f"consecutive words matching the source in order "
                        f"(default {VERBATIM_SHINGLE})")

    g = ap.add_argument_group("transcription")
    g.add_argument("--whisper-model", default=os.getenv("WHISPER_MODEL", "medium.en"),
                   help="faster-whisper model name (env: WHISPER_MODEL)")
    g.add_argument("--device", choices=["auto", "cuda", "cpu"],
                   default=os.getenv("WHISPER_DEVICE", "auto").strip() or "auto",
                   help="auto picks cuda when CTranslate2 sees a GPU (env: WHISPER_DEVICE)")
    g.add_argument("--compute-type", default=os.getenv("WHISPER_COMPUTE_TYPE", "").strip() or None,
                   help="e.g. float16 on GPU, int8 on CPU (env: WHISPER_COMPUTE_TYPE)")
    g.add_argument("--beam-size", type=int, default=int(os.getenv("WHISPER_BEAM_SIZE", "5")),
                   help="env: WHISPER_BEAM_SIZE")
    g.add_argument("--vad", dest="vad", action="store_true", default=None,
                   help="enable VAD filtering (env: WHISPER_VAD_FILTER)")
    g.add_argument("--no-vad", dest="vad", action="store_false",
                   help="disable VAD (default here — VAD can silently drop quiet speech, "
                        "which would read as missing content in the audit)")
    g.add_argument("--language", default=os.getenv("WHISPER_LANGUAGE", "en").strip() or None)

    p = ap.add_argument_group("paths")
    p.add_argument("--input-pdf")
    p.add_argument("--audio-dir")
    p.add_argument("--work-dir")
    p.add_argument("--out-dir")
    p.add_argument("--source-text", help="verified transcription of the PDF, if you have one")

    args = ap.parse_args()
    configure_paths(args)

    vad = env_flag("WHISPER_VAD_FILTER", False) if args.vad is None else args.vad
    device, compute_type, reason = resolve_device(args.device, args.compute_type)
    tr = Transcriber(
        model_name=args.whisper_model,
        device=device,
        compute_type=compute_type,
        beam_size=args.beam_size,
        vad_filter=vad,
        language=args.language,
    )

    if args.check:
        return preflight(tr, reason, args.ocr_gate, args.lex_gate)

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("[1/5] reading source document", file=sys.stderr)
    source, provenance, ocr_conf, ocr_lines = load_source(args.force_ocr)
    print(f"      {provenance}", file=sys.stderr)

    lex, offenders = lexical_validity(source)
    if lex >= 0:
        print(f"      dictionary validity {lex:.1f}% ({len(offenders)} non-words)",
              file=sys.stderr)

    gate_failed = (ocr_conf < args.ocr_gate) or (0 <= lex < args.lex_gate)
    gate_bypassed = gate_failed and args.ignore_ocr_gate

    if gate_failed and not args.ignore_ocr_gate:
        # Still transcribe: it is the slow half, it is cached, and the operator will
        # want it ready for the re-run after correcting the text.
        print(f"      source text rejected (confidence {ocr_conf:.1f}%/{args.ocr_gate:.0f}%, "
              f"dictionary {lex:.1f}%/{args.lex_gate:.0f}%) — will not score coverage",
              file=sys.stderr)
        print(f"[2/5] transcribing audio with {tr.model_name} on {tr.device}/{tr.compute_type} ({reason})",
              file=sys.stderr)
        lessons, durations = load_lessons(tr, args.force_transcribe)
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        md = render_ocr_refusal(source, provenance, ocr_conf, args.ocr_gate,
                                lex, args.lex_gate, offenders,
                                ocr_lines, lessons, durations, tr)
        REPORT_MD.write_text(md, encoding="utf-8")
        print(f"\nwrote {REPORT_MD}  (source text rejected — see 'Fix it')", file=sys.stderr)
        return 2

    all_claims = split_claims(source)
    # Front matter is dropped before matching rather than filtered out of each total
    # afterwards, so every downstream count is right by construction.
    if args.keep_front_matter:
        claims, front_matter = all_claims, []
    else:
        front_matter = [c for c in all_claims if is_boilerplate(c.text)]
        claims = [c for c in all_claims if not is_boilerplate(c.text)]
    print(f"      {len(claims)} source statements"
          + (f" ({len(front_matter)} excluded as front matter)" if front_matter else ""),
          file=sys.stderr)

    print(f"[2/5] transcribing audio with {tr.model_name} on {tr.device}/{tr.compute_type} ({reason})", file=sys.stderr)
    lessons, durations = load_lessons(tr, args.force_transcribe)

    print("[3/5] matching", file=sys.stderr)
    units = build_units(lessons)
    match(claims, units)
    dups = near_duplicates(units)
    lifted = verbatim_runs(source, lessons, args.verbatim_shingle)
    print(f"      {lifted['percent']:.1f}% of narration is verbatim from the source "
          f"(runs of {args.verbatim_shingle}+ words)", file=sys.stderr)

    verdict = None
    digest = signal_digest(claims, units, dups, lifted)
    (WORK_DIR / "signals.txt").write_text(digest, encoding="utf-8")

    if args.adjudication:
        print(f"[4/5] loading adjudication from {args.adjudication}", file=sys.stderr)
        verdict = json.loads(Path(args.adjudication).read_text(encoding="utf-8"))
    elif not args.no_llm:
        print("[4/5] adjudicating with Claude", file=sys.stderr)
        verdict = adjudicate(source, lessons, digest)
    else:
        print("[4/5] skipping adjudication (--no-llm)", file=sys.stderr)

    print("[5/5] writing report", file=sys.stderr)
    md = render(source, provenance, ocr_conf, args.ocr_gate, lex, args.lex_gate,
                gate_bypassed, claims, units, lessons, dups, durations, verdict, tr,
                lifted, front_matter)
    REPORT_MD.write_text(md, encoding="utf-8")
    REPORT_JSON.write_text(json.dumps({
        "source": source,
        "provenance": provenance,
        "ocr_confidence": ocr_conf,
        "ocr_gate": args.ocr_gate,
        "lexical_validity": lex,
        "lexical_gate": args.lex_gate,
        "lexical_offenders": offenders,
        "ocr_gate_bypassed": gate_bypassed,
        "runtime": {
            "whisper_model": tr.model_name,
            "device": tr.device,
            "compute_type": tr.compute_type,
            "device_reason": reason,
            "beam_size": tr.beam_size,
            "vad_filter": tr.vad_filter,
            "language": tr.language,
            "embed_model": EMBED_MODEL_NAME,
            "embed_device": torch_device(),
            "cuda_devices_visible": cuda_devices(),
        },
        "verbatim": lifted,
        "front_matter_excluded": [c.as_dict() for c in front_matter],
        "claims": [c.as_dict() for c in claims],
        "units": [asdict(u) for u in units],
        "near_duplicates": [
            {"a": {"lesson": a.lesson, "text": a.text},
             "b": {"lesson": b.lesson, "text": b.text},
             "similarity": s}
            for a, b, s in dups
        ],
        "durations": durations,
        "adjudication": verdict,
    }, indent=2), encoding="utf-8")

    print(f"\nwrote {REPORT_MD}", file=sys.stderr)
    print(f"wrote {REPORT_JSON}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
