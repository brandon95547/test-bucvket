#!/usr/bin/env python3
"""
analyze_course.py — audit an audio course against its source document.

Compares the MP3s in output/ against input/original.pdf and writes a report
answering two questions:

  1. Is the narration re-worded, or is it the book read aloud? What percentage of
     the spoken words are word-for-word from the book?
  2. Is any of the book's content missing from the audio, and exactly what?

"The book" means its body text. Title page, copyright page, table of contents and
back matter (appendix, bibliography, index) are excluded before anything is measured
— nobody narrates those, and counting them as missing would understate coverage.
The report lists every page that was dropped and why.

Pipeline
--------
  PDF  --PyMuPDF+tesseract-->  page text --strip non-body--> body --clause split--> claims
  MP3s --faster-whisper------>  lesson transcripts --sentence split--> units
  body x narration --word-run matching--------> how much is verbatim  (question 1)
  claims x units  --MiniLM embeddings + lexical/entity checks--> coverage  (question 2)

No model judges the result: both numbers are computed, so the same inputs always
give the same report. Everything expensive is cached under work/ so re-runs are cheap.

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
    # de-hyphenate words split across lines. The space before the hyphen is not a typo:
    # justified academic typesetting breaks as "Oxy rhyn -\nchus", and without allowing
    # it the tail lands in the next sentence as a bare fragment ("chus, and about to…").
    text = re.sub(r"(\w)[ \t]*-[ \t]*\n[ \t]*(\w)", r"\1\2", text)
    # keep paragraph structure, collapse in-paragraph wrapping. \f is excluded from the
    # blank-line collapse by hand: it is whitespace, so "\n\f\n" matches \n\s*\n and the
    # page break would be normalized away before body_text() ever saw it.
    text = re.sub(r"\n[ \t\r\v]*\n", "\n\n", text)
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


# A page break in the source text. pdftotext writes one between pages and this tool
# emits one per rendered/extracted page, so page structure survives into the string
# that everything downstream reads.
PAGE_SEP = "\f"

# Headings that open back matter. A book's appendices, bibliography and index sit at
# the END, so the first page whose heading matches ends the body: everything from
# there on is apparatus. Widen or narrow this list to change what "the book's content"
# means — whatever it drops is listed in the report, so a wrong call is visible rather
# than silent.
BACK_MATTER_HEADINGS = (
    r"appendix(?:\s+[a-z0-9]+)?",
    r"bibliography",
    r"index",
    r"works cited",
)

_DOT_LEADER = re.compile(r"\.\s*\.\s*\.\s*\.")
_FOLIO = re.compile(r"^(?:\d{1,4}|[ivxlcdm]{1,7})$", re.I)


def _page_lines(page: str) -> list[str]:
    return [l.strip() for l in page.splitlines() if l.strip()]


def _is_contents_page(page: str) -> bool:
    """A table of contents is headings joined to page numbers by dot leaders.

    The "Table of Contents" heading only appears on the FIRST of what may be several
    contents pages, so the leaders — not the heading — are the reliable signal.
    """
    lines = _page_lines(page)
    if not lines:
        return False
    if re.match(r"^(table of )?contents?\b", lines[0], re.I):
        return True
    return sum(1 for l in lines if _DOT_LEADER.search(l)) >= 3


def _is_prose(page: str) -> bool:
    """Does this page read like the book, rather than like its packaging?

    Half-title, series and title pages are lists of names set large — many words, no
    sentences. Requiring both length and sentence-ends separates them from chapter
    text without needing to know what any particular book puts up front.
    """
    words = len(re.findall(r"[A-Za-z'’]+", page))
    sentences = len(re.findall(r"[a-z]{2}[.!?](?:\s|$)", page))
    return words >= 120 and sentences >= 3


def _opens_back_matter(page: str) -> str | None:
    """The heading that ends the body, if this page carries one."""
    for line in _page_lines(page)[:3]:
        for pat in BACK_MATTER_HEADINGS:
            if re.fullmatch(pat, line, re.I):
                return line
    return None


def _running_heads(pages: list[str]) -> set[str]:
    """Chapter/section names reprinted at the top of every page.

    They are navigation, not prose: left in, each one becomes a repeated 'claim' that
    the narration is then marked as failing to cover. Detected by repetition rather
    than by pattern, so this needs no per-book configuration.
    """
    counts: dict[str, int] = {}
    for page in pages:
        for line in _page_lines(page)[:2]:
            if len(line) <= 70 and not line[-1:] in ".:;,":
                counts[line.lower()] = counts.get(line.lower(), 0) + 1
    return {head for head, n in counts.items() if n >= 3}


def body_text(source: str) -> tuple[str, list[dict]]:
    """The book's actual content, and a record of everything dropped to get there.

    Answers "is anything missing from the course" honestly by first deciding what
    "the book" means: not its title page, copyright notice, table of contents or
    appendices — nobody narrates those, and counting them as missing content would
    understate coverage by whatever share of the PDF they happen to occupy.

    Returns (text, excluded) where each excluded entry says which page went and why.
    """
    pages = source.split(PAGE_SEP)
    heads = _running_heads(pages)
    kept: list[str] = []
    excluded: list[dict] = []
    back_matter_from: str | None = None
    in_front_matter = True          # until the first page that reads like the book

    for n, page in enumerate(pages, start=1):
        preview = " ".join(_page_lines(page)[:2])[:80].replace("|", "\\|")

        if back_matter_from is not None:
            excluded.append({"page": n, "reason": f"back matter ({back_matter_from})",
                             "preview": preview})
            continue

        opener = _opens_back_matter(page)
        if opener:
            back_matter_from = opener
            excluded.append({"page": n, "reason": f"back matter ({opener})",
                             "preview": preview})
            continue

        if _is_contents_page(page):
            excluded.append({"page": n, "reason": "table of contents", "preview": preview})
            continue

        if is_boilerplate(page):
            excluded.append({"page": n, "reason": "front matter (copyright/ISBN)",
                             "preview": preview})
            continue

        # Front matter only counts as front matter until the book starts. After that a
        # short page is a short page — a chapter opening or a plate — not packaging.
        if in_front_matter:
            if not _is_prose(page):
                excluded.append({"page": n, "reason": "front matter (no body text)",
                                 "preview": preview})
                continue
            in_front_matter = False

        body = [l for l in _page_lines(page)
                if not _FOLIO.match(l) and l.lower() not in heads]
        if not body:
            excluded.append({"page": n, "reason": "no body text", "preview": preview})
            continue
        kept.append("\n".join(body))

    return "\n\n".join(kept), excluded


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


def ocr_pdf(pdf: Path, force: bool) -> tuple[str, float, list[OcrLine], str]:
    """Read the PDF. Returns (text, mean confidence 0-100, per-line detail, method).

    method is "text-layer" when the text came out of the PDF losslessly and "ocr"
    when it was read off a page image. Callers need the difference: the confidence
    and dictionary gates exist to catch OCR misreads, and there are none to catch
    in a text layer.
    """
    cache = WORK_DIR / "ocr.json"
    if cache.exists() and not force:
        d = json.loads(cache.read_text(encoding="utf-8"))
        # A cache with no "method" was written before the text layer was joined on
        # PAGE_SEP. Its text has no page breaks at all, so body_text() sees the whole
        # book as a single page — and, finding the contents page's dot leaders in it,
        # throws the book away as a table of contents. Re-read the PDF instead of
        # trusting it; that costs one extraction and is silently wrong otherwise.
        if d.get("method"):
            lines = [OcrLine(tuple(l["key"]), l["text"], l["conf"], l["run"]) for l in d["lines"]]
            return d["text"], d["confidence"], lines, d["method"]
        print("      ignoring pre-page-break ocr.json cache — re-reading the PDF",
              file=sys.stderr)

    if not shutil.which("tesseract"):
        raise SystemExit("need tesseract on PATH")

    # PDF -> page images via PyMuPDF rather than poppler's pdftoppm, so the only
    # system binary this tool needs is tesseract itself. phansora-api rasterizes
    # the same way (products/spokenverse/services/pdf_render.py), which is why the
    # venv named in README.md already satisfies this.
    try:
        import fitz  # PyMuPDF
    except ImportError:
        raise SystemExit(
            "need PyMuPDF to read PDFs: pip install pymupdf "
            "(already present in the phansora-api venv — see README.md)"
        )

    doc = fitz.open(str(pdf))
    try:
        # An embedded text layer beats any amount of OCR — use it when the PDF has one.
        # Joined on PAGE_SEP, not "\n": body_text() needs the page boundaries to tell a
        # contents page or an appendix from the chapter next to it.
        embedded = PAGE_SEP.join(page.get_text() for page in doc)
        if len(embedded.strip()) > 200:
            lines = [OcrLine((0, 0, 0, i), t.strip(), 100.0, "pdf-text-layer")
                     for i, t in enumerate(embedded.splitlines()) if t.strip()]
            cache.write_text(json.dumps(
                {"text": embedded, "confidence": 100.0, "method": "text-layer",
                 "lines": [{"key": list(l.key), "text": l.text, "conf": l.conf, "run": l.run}
                           for l in lines]}, indent=2), encoding="utf-8")
            return embedded, 100.0, lines, "text-layer"

        render_dir = WORK_DIR / "pages"
        render_dir.mkdir(parents=True, exist_ok=True)
        # Grayscale at OCR_RENDER_DPI, matching what pdftoppm -gray -r produced.
        # Zero-padded like pdftoppm so the pages sort in reading order, and collected
        # as an explicit list rather than re-globbed: _preprocess() drops its own
        # "__prep.png" beside each page, which a glob picks up as if it were one.
        matrix = fitz.Matrix(OCR_RENDER_DPI / 72.0, OCR_RENDER_DPI / 72.0)
        pad = max(2, len(str(doc.page_count)))
        page_pngs: list[Path] = []
        for n, page in enumerate(doc, start=1):
            out = render_dir / f"pg-{n:0{pad}d}.png"
            page.get_pixmap(matrix=matrix, colorspace=fitz.csGRAY, alpha=False).save(str(out))
            page_pngs.append(out)
    finally:
        doc.close()

    all_lines: list[OcrLine] = []
    for page_no, png in enumerate(page_pngs):
        prepped = _preprocess(png)
        runs = []
        for img, label in ((png, "raw"), (prepped, "prep")):
            for psm in OCR_PSMS:
                runs.append(_tesseract_lines(img, psm, f"{label}/psm{psm}", page_no))
        merged, _ = _vote(runs)
        all_lines.extend(merged)

    # Page-separated for body_text(); OcrLine.key[0] is the page the line came from.
    by_page: dict[int, list[str]] = {}
    for l in all_lines:
        by_page.setdefault(l.key[0], []).append(l.text)
    text = PAGE_SEP.join("\n".join(by_page[p]) for p in sorted(by_page))
    conf = sum(l.conf for l in all_lines) / len(all_lines) if all_lines else 0.0
    cache.write_text(json.dumps(
        {"text": text, "confidence": conf, "method": "ocr",
         "lines": [{"key": list(l.key), "text": l.text, "conf": l.conf, "run": l.run}
                   for l in all_lines]}, indent=2), encoding="utf-8")
    return text, conf, all_lines, "ocr"


def load_source(force_ocr: bool) -> tuple[str, str, float, list[OcrLine], str]:
    """Returns (raw page-separated text, provenance, OCR confidence 0-100, line detail).

    Deliberately NOT normalized: body_text() reads page breaks and line breaks to tell a
    contents page from a chapter and a running header from a sentence, and normalizing
    first unwraps every page into one long line. Callers normalize what they keep.
    """
    if SIDECAR_SOURCE and SIDECAR_SOURCE.exists():
        raw = SIDECAR_SOURCE.read_text(encoding="utf-8")
        return raw, f"corrected transcription supplied via --source-text ({SIDECAR_SOURCE.name})", 100.0, [], "supplied"

    pdf = INPUT_PDF
    if not pdf.exists():
        raise SystemExit(f"missing {pdf}")

    raw, conf, lines, method = ocr_pdf(pdf, force_ocr)
    if method == "text-layer":
        provenance = f"{pdf.name}'s embedded text layer, extracted losslessly with PyMuPDF"
    else:
        provenance = (f"{len(OCR_PSMS)}-mode tesseract OCR of {pdf.name}, raw + deskewed/thresholded, "
                      f"per-line majority vote (mean confidence {conf:.1f}%)")
    return raw, provenance, conf, lines, method


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

    # Either side being empty means an earlier step read nothing; embedding an empty
    # list yields a shapeless array that only fails at the matmul, far from the cause.
    if not claims or not units:
        raise SystemExit(
            f"nothing to match: {len(claims)} source statement(s) against "
            f"{len(units)} narrated sentence(s)"
        )

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


# ---------------------------------------------------------------------------
# stage 4 — report
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


def _originality_reading(verbatim_pct: float) -> str:
    """Plain-English reading of the verbatim share.

    Bands, not a legal opinion: this measures word-for-word overlap, which is evidence
    about copying but is not the whole of what "a copy" means to a lawyer. Say what was
    measured and let the reader draw the conclusion.
    """
    if verbatim_pct < 5:
        return ("The narration is told in its own words. Almost nothing in the audio "
                "matches the book word for word.")
    if verbatim_pct < 15:
        return ("The narration is substantially re-worded. The word-for-word overlap "
                "is small and, at this level, is usually quotation rather than copying.")
    if verbatim_pct < 30:
        return ("The narration is re-worded, but a meaningful share of it is word for "
                "word. Read the longest runs below and satisfy yourself that they are "
                "quotations you meant to keep.")
    return ("A large share of the narration is word for word. At this level the audio "
            "reads as the book being read aloud in places, not retold.")


def _coverage_reading(present_pct: float, missing: int) -> str:
    if missing == 0:
        return "Every statement in the book's body text is represented in the audio."
    if present_pct >= 90:
        return (f"Nearly all of the book is present. {missing} statement(s) have no "
                f"match in the audio — listed below.")
    if present_pct >= 70:
        return (f"Most of the book is present, but {missing} statement(s) are absent "
                f"from the audio entirely.")
    return (f"Substantial parts of the book are not in the audio: {missing} statement(s) "
            f"have no match.")


def render(body: str, provenance: str, ocr_conf: float, gate: float,
           lex: float, lex_gate: float, gate_bypassed: bool,
           claims: list[Claim], lessons: list[tuple[str, str]],
           tr: Transcriber, lifted: dict,
           excluded: list[dict], shingle: int) -> str:
    """The whole report: two questions, answered, plus what they were measured against."""
    L: list[str] = []
    A = L.append

    covered = [c for c in claims if c.status == "covered"]
    partial = [c for c in claims if c.status == "partial"]
    missing = [c for c in claims if c.status == "missing"]
    total = len(claims)
    present_pct = pct(len(covered) + len(partial), total)

    verbatim_pct = lifted["percent"]
    reworded_pct = 100.0 - verbatim_pct
    longest = max((r["length"] for r in lifted["runs"]), default=0)

    A(f"# Course audit — {INPUT_PDF.name}")
    A("")
    A(f"{len(lessons)} audio lesson(s) against the body text of {INPUT_PDF.name}.")
    A("")

    if gate_bypassed:
        A("> **The source text failed its quality gates and was scored anyway "
          "(`--ignore-ocr-gate`).** Both numbers below are measured against text that "
          "may be misread. Treat them as indicative, not final.")
        A("")

    # ---- question 1 -------------------------------------------------------
    A("## 1. Is the audio re-worded, or a copy?")
    A("")
    A(f"### {reworded_pct:.1f}% re-worded")
    A("")
    A(f"{verbatim_pct:.1f}% of the narration — {lifted['lifted']:,} of "
      f"{lifted['words']:,} spoken words — appears in the book word for word, counting "
      f"any run of {shingle} or more consecutive words that match in order. "
      f"The longest single unbroken run is **{longest} words**.")
    A("")
    A(_originality_reading(verbatim_pct))
    A("")

    if lifted["per_lesson"]:
        A("| Lesson | Spoken words | Word-for-word | Re-worded | Longest run |")
        A("|---|---:|---:|---:|---:|")
        for r in lifted["per_lesson"]:
            A(f"| {r['lesson']} | {r['words']:,} | {r['percent']:.1f}% | "
              f"{100.0 - r['percent']:.1f}% | {r['longest_run']} |")
        A("")

    long_runs = [r for r in lifted["runs"] if r["length"] >= shingle * 2][:10]
    if long_runs:
        A(f"<details><summary>The {len(long_runs)} longest word-for-word passages</summary>")
        A("")
        for r in long_runs:
            A(f"- **{r['length']} words** · {r['lesson']}")
            A(f"  > {r['text']}")
        A("")
        A("</details>")
        A("")
        A("_A book that quotes scripture or another primary source will show runs here "
          "when the course quotes the same passage, without either having copied the "
          "book's own writing. Check what the long runs actually are before reading "
          "them as copying._")
        A("")

    # ---- question 2 -------------------------------------------------------
    A("## 2. Is any of the book's content missing?")
    A("")
    A(f"### {present_pct:.1f}% of the book is present")
    A("")
    A(f"The book's body text breaks into {total} checkable statements. "
      f"{len(covered)} are clearly present in the audio, {len(partial)} partly, "
      f"and **{len(missing)} are absent**.")
    A("")
    A(_coverage_reading(present_pct, len(missing)))
    A("")
    A("| | Statements | Share |")
    A("|---|---:|---:|")
    A(f"| Covered | {len(covered)} | {pct(len(covered), total):.1f}% |")
    A(f"| Partly covered | {len(partial)} | {pct(len(partial), total):.1f}% |")
    A(f"| Missing | {len(missing)} | {pct(len(missing), total):.1f}% |")
    A("")

    if missing:
        shown = missing[:60]
        A(f"### What is missing ({len(missing)} statement(s))")
        A("")
        if len(shown) < len(missing):
            A(f"_First {len(shown)}; the rest are in `report.json`._")
            A("")
        for c in shown:
            A(f"- {c.text}")
        A("")

    if partial:
        shown = partial[:40]
        A(f"<details><summary>Partly covered ({len(partial)}) — the idea is there, "
          f"detail is not</summary>")
        A("")
        for c in shown:
            gaps = []
            if c.dropped_numbers:
                gaps.append("numbers dropped: " + ", ".join(map(str, c.dropped_numbers)))
            if c.dropped_entities:
                gaps.append("names dropped: " + ", ".join(map(str, c.dropped_entities)))
            A(f"- {c.text}")
            if gaps:
                A(f"  - _{'; '.join(gaps)}_")
        if len(shown) < len(partial):
            A(f"- _…and {len(partial) - len(shown)} more, in `report.json`._")
        A("")
        A("</details>")
        A("")

    # ---- what "the book" means -------------------------------------------
    A("## What counted as \"the book\"")
    A("")
    if excluded:
        A(f"{len(excluded)} page(s) were left out of the comparison — front matter, "
          f"contents and back matter are not content anybody narrates, and counting "
          f"them as missing would understate coverage:")
        A("")
        A("| Page | Left out because | Starts |")
        A("|---:|---|---|")
        for e in excluded:
            A(f"| {e['page']} | {e['reason']} | {e['preview']} |")
        A("")
    else:
        A("Every page of the PDF was treated as body text — no contents page, "
          "front matter or appendix was detected.")
        A("")
    A(f"Running headers and page numbers are stripped from the pages that were kept. "
      f"Body text used: {len(bare_words(body)):,} words.")
    A("")

    # ---- method -----------------------------------------------------------
    A("## How this was measured")
    A("")
    A(f"- **Source text** — {provenance}.")
    if ocr_conf < 100:
        A(f"- **OCR quality** — {ocr_conf:.1f}% mean word confidence (gate {gate:.0f}%), "
          f"{lex:.1f}% of words found in a dictionary (gate {lex_gate:.0f}%).")
    A(f"- **Audio** — transcribed with faster-whisper `{tr.model_name}` on "
      f"{tr.device}/{tr.compute_type}"
      + (f", VAD off" if not tr.vad_filter else "") + ".")
    A(f"- **Re-worded %** — the share of spoken words NOT inside a run of {shingle}+ "
      f"consecutive words matching the book in order.")
    A(f"- **Present %** — each book statement is matched against every spoken sentence "
      f"using sentence-embedding similarity ({EMBED_MODEL_NAME}) plus a check that the "
      f"numbers and names in it survived. Covered at ≥{COVERED_EMB:.2f} similarity, "
      f"partial at ≥{PARTIAL_EMB:.2f}.")
    A("")
    A("_These are measurements of this parse of this text, not legal conclusions. "
      "The re-worded percentage is evidence about copying, not a ruling on it._")
    A("")

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

    # Which python is answering matters more than any row below it: a missing package
    # here usually means the wrong interpreter, not an unbuilt venv.
    print(f"\ninterpreter\n       {sys.executable}")

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
    for name, required in (("tesseract", need_pdf), ("ffprobe", False)):
        found = shutil.which(name)
        if required:
            row(name, found or "NOT FOUND", bool(found))
        else:
            print(f"  {'ok ' if found else '--  '} {name:<26} "
                  f"{found or 'not found (optional)'}")

    print("\npython packages")
    for mod, required in (("faster_whisper", True), ("ctranslate2", True),
                          ("sentence_transformers", True), ("numpy", True),
                          ("fitz", need_pdf), ("torch", False)):
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

    print("\n" + "-" * 62)
    print("READY" if ok else "NOT READY — fix the FAIL rows above")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="print resolved device/model/deps and exit without doing work")
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
    o.add_argument("--whole-document", "--keep-front-matter", dest="keep_front_matter",
                   action="store_true",
                   help="measure against every page, including title/copyright pages, "
                        "the table of contents and any appendix (default: body text "
                        "only, with each dropped page listed in the report)")

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

    print("[1/4] reading source document", file=sys.stderr)
    raw_source, provenance, ocr_conf, ocr_lines, method = load_source(args.force_ocr)
    page_count = len(raw_source.split(PAGE_SEP))
    source = normalize_source(raw_source)
    print(f"      {provenance}  ({page_count} page(s))", file=sys.stderr)

    # What "the book" is, decided before anything is measured against it: contents pages
    # and appendices are not content anybody narrates, and leaving them in would count
    # them as missing and understate coverage.
    if args.keep_front_matter:
        body, excluded = source, []
    else:
        body_raw, excluded = body_text(raw_source)
        body = normalize_source(body_raw)
    for e in excluded:
        print(f"      excluded page {e['page']}: {e['reason']}", file=sys.stderr)

    # Nothing left to compare against. This is always a reading fault, never a real
    # book: say so here rather than let an empty claim list surface as a numpy shape
    # error three steps later.
    if not body.strip():
        raise SystemExit(
            f"every page of {page_count} was excluded as front/back matter — there is no "
            "body text to score.\n"
            "  A one-page count above means the page breaks were lost, so the whole book "
            "reads as a single page.\n"
            "  Re-read the source with --force-ocr, or keep everything with "
            "--keep-front-matter."
        )

    # Gates are measured on the body, not the whole PDF: a contents page is dot leaders
    # and a copyright page is legal boilerplate, and neither says anything about whether
    # the text being scored was read correctly.
    lex, offenders = lexical_validity(body)
    if lex >= 0:
        print(f"      dictionary validity {lex:.1f}% ({len(offenders)} non-words)",
              file=sys.stderr)

    # ...and they only apply to OCR. Both gates are proxies for "did tesseract misread
    # this"; text lifted straight out of the PDF's own text layer has no misreads to
    # find, and an academic book's vocabulary would fail the dictionary gate on merit.
    gate_failed = method == "ocr" and ((ocr_conf < args.ocr_gate) or (0 <= lex < args.lex_gate))
    gate_bypassed = gate_failed and args.ignore_ocr_gate
    if method != "ocr":
        print(f"      quality gates not applicable ({method}) — nothing was OCR'd",
              file=sys.stderr)

    if gate_failed and not args.ignore_ocr_gate:
        # Still transcribe: it is the slow half, it is cached, and the operator will
        # want it ready for the re-run after correcting the text.
        print(f"      source text rejected (confidence {ocr_conf:.1f}%/{args.ocr_gate:.0f}%, "
              f"dictionary {lex:.1f}%/{args.lex_gate:.0f}%) — will not score coverage",
              file=sys.stderr)
        print(f"[2/4] transcribing audio with {tr.model_name} on {tr.device}/{tr.compute_type} ({reason})",
              file=sys.stderr)
        lessons, durations = load_lessons(tr, args.force_transcribe)
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        md = render_ocr_refusal(source, provenance, ocr_conf, args.ocr_gate,
                                lex, args.lex_gate, offenders,
                                ocr_lines, lessons, durations, tr)
        REPORT_MD.write_text(md, encoding="utf-8")
        print(f"\nwrote {REPORT_MD}  (source text rejected — see 'Fix it')", file=sys.stderr)
        return 2

    claims = split_claims(body)
    print(f"      {len(claims)} statements from {page_count - len(excluded)} "
          f"body page(s)", file=sys.stderr)

    print(f"[2/4] transcribing audio with {tr.model_name} on {tr.device}/{tr.compute_type} ({reason})", file=sys.stderr)
    lessons, durations = load_lessons(tr, args.force_transcribe)

    print("[3/4] matching", file=sys.stderr)
    units = build_units(lessons)
    match(claims, units)
    lifted = verbatim_runs(body, lessons, args.verbatim_shingle)
    print(f"      {100.0 - lifted['percent']:.1f}% of narration is re-worded "
          f"({lifted['percent']:.1f}% verbatim, runs of {args.verbatim_shingle}+ words)",
          file=sys.stderr)
    print(f"      {pct(sum(1 for c in claims if c.status != 'missing'), len(claims)):.1f}% "
          f"of the book is present in the audio", file=sys.stderr)

    print("[4/4] writing report", file=sys.stderr)
    md = render(body, provenance, ocr_conf, args.ocr_gate, lex, args.lex_gate,
                gate_bypassed, claims, lessons, tr, lifted,
                excluded, args.verbatim_shingle)
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
        # The two headline answers, so a caller does not have to recompute them.
        "reworded_percent": 100.0 - lifted["percent"],
        "present_percent": pct(sum(1 for c in claims if c.status != "missing"), len(claims)),
        "verbatim": lifted,
        "excluded_pages": excluded,
        "claims": [c.as_dict() for c in claims],
        "units": [asdict(u) for u in units],
        "durations": durations,
    }, indent=2), encoding="utf-8")

    print(f"\nwrote {REPORT_MD}", file=sys.stderr)
    print(f"wrote {REPORT_JSON}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
