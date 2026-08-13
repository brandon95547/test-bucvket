# test-bucvket — course audit harness

`analyze_course.py` audits a generated audio course against the source document it was
built from, and answers two questions:

1. **Is the audio re-worded, or is it the book read aloud?** What percentage of the
   spoken words are word-for-word from the book — the number that answers "someone
   could say this is just a literal copy of that book".
2. **Is any of the book's content missing?** What percentage of the book is present in
   the audio, and exactly which statements are not.

```
input/*.pdf  ──PyMuPDF + tesseract──▶  page text ──strip non-body──▶ body ──▶ claims
output/*.mp3 ──faster-whisper───────▶  transcripts   ──sentence split──▶  units

     body × narration ──word-run matching──▶  how much is verbatim     (question 1)
     claims × units   ──MiniLM embeddings──▶  what is covered/missing  (question 2)
```

**No LLM is involved.** Both numbers are computed, so the same inputs always produce the
same report and it runs on a box with no API credentials.

### What counts as "the book"

Coverage is measured against the **body text only**. Before anything is compared, the
script drops the title and copyright pages, the table of contents, and any back matter
(appendix, bibliography, index) — nobody narrates those, and leaving them in would count
them as missing content and understate coverage.

That filtering is reported, not hidden: `REPORT.md` lists every page that was dropped
and why, so a wrong call is visible. `--whole-document` disables it. The back-matter
headings live in `BACK_MATTER_HEADINGS` in the script if a book needs a different list.

Everything expensive is cached in `work/`, so re-runs are cheap — which is also the main
way to get a wrong answer. See [Read this before your first run](#read-this-before-your-first-run).

---

## Installing

You need an interpreter that can import `faster_whisper`, `ctranslate2`,
`sentence_transformers` and `torch`. A bare `python3` cannot. Either reuse a venv that
already has them or build one from `requirements.txt` — both are below.

**System packages first.** These are not pip-installable, and OCR does not run without
`tesseract`:

```bash
sudo apt install tesseract-ocr ffmpeg wamerican wbritish     # Debian/Ubuntu
sudo dnf install tesseract ffmpeg-free words                 # RHEL/CentOS/Fedora
```

`tesseract` is the only required binary. Rendering PDF pages is PyMuPDF's job (a pip
package, in `requirements.txt`), not poppler's — so there is nothing to install as root
for the PDF side, which matters on a box where you would rather not.

`ffmpeg` supplies `ffprobe`, used only for audio duration when Whisper doesn't report it.
The two word lists back the lexical gate — without them `--check` prints
`dictionary gate DISABLED`, and bad OCR stops being caught.

**Option A — reuse the phansora-api virtualenv. Nothing to install.** It already
satisfies every pin in `requirements.txt`, torch included:

```bash
cd /home/crimson/sites/test-bucvket
/home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py --check
```

**Option B — a venv of your own.** Python 3.11:

```bash
cd /home/crimson/sites/test-bucvket
python3.11 -m venv .venv

# GPU-less box: get the CPU torch build first, or pip drags in ~2.5 GB of unused
# CUDA wheels. Skip this line if you have a GPU.
.venv/bin/pip install torch==2.13.0 --index-url https://download.pytorch.org/whl/cpu

.venv/bin/pip install -r requirements.txt
.venv/bin/python analyze_course.py --check
```

Roughly 3 GB installed. The MiniLM embedding model and the Whisper weights are *not* part
of that — they download from HuggingFace on first use, into `~/.cache/huggingface`.

The commands below use the phansora-api interpreter; substitute `.venv/bin/python`
throughout if you went with option B.

---

## Running it

```bash
cd /home/crimson/sites/test-bucvket

# 1. Preflight — resolves paths, binaries, packages and device, then exits.
/home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py --check

# 2. The real run.
/home/crimson/sites/phansora-api/.venv/bin/python analyze_course.py \
    --input-pdf input/forbidden-oracles-gospel-of-the-lots.pdf \
    --force-ocr
```

Always run `--check` first. It is instant, and it is the difference between finding a
missing binary now and finding it after a long transcription pass.

`--input-pdf` is needed because the script defaults to `input/original.pdf` and the PDF
sitting there has a different name. `--force-ocr` is explained below.

---

## Read this before your first run

**This folder currently holds artefacts from more than one job.** Nothing here is broken,
but a naive re-run will produce a confident, wrong report.

| Path | What is actually in it |
|---|---|
| `input/` | *Forbidden Oracles — Gospel of the Lots of Mary*, 15 pages |
| `output/` | 2 MP3s for that same course |
| `work/ocr.json`, `work/pages/` | OCR of a **different** book — *The Book of Wisdom* |
| `work/transcripts/` | 8 lesson transcripts from that **same other** course |
| `REPORT.md`, `report.json` | Output of that other run, not of `input/` — both are overwritten by the next run |
| `source_corrected.txt` | A 1940 business letter. Unrelated to either. |

Two consequences:

- **`work/ocr.json` is a single unkeyed cache file.** It is reused regardless of which PDF
  you pass, so without `--force-ocr` the script will audit the current MP3s against the
  *Book of Wisdom* text and report near-total failure. This is the trap.
- **Do not pass `--source-text source_corrected.txt`.** The flag takes a verified
  transcription of *your* PDF; that file is neither. `--check` will happily report it as
  `ok`, because it only checks that the file exists.

The cleanest start is to empty the cache rather than remember the flag:

```bash
rm -rf work/            # regenerated on the next run; it is gitignored
```

Transcripts are cached per audio filename, so those are safe — the two MP3s in `output/`
simply are not in there yet.

---

## Requirements

| | |
|---|---|
| Interpreter | `/home/crimson/sites/phansora-api/.venv/bin/python`, or a Python 3.11 venv built from `requirements.txt` |
| Binaries | `tesseract` (required, PDF path only) · `ffprobe` (used when present) |
| Packages | `faster_whisper`, `ctranslate2`, `sentence_transformers`, `numpy`, `torch` · `fitz` (PyMuPDF) for the PDF path · `pillow` + `scipy` sharpen OCR |

`requirements.txt` holds the exact versions this has been run against, with the reason for
each one. `--check` prints the whole table above with a resolved value per row, so treat
its output as the source of truth rather than this table.

---

## Runtime

Device selection is `auto`: CUDA with float16 when CTranslate2 reports a usable GPU,
otherwise CPU with int8. A CUDA load failure at runtime falls back to CPU rather than
aborting the job.

**On this machine `--check` reports 0 CUDA devices, so it runs `cpu / int8`.** Whisper
transcription dominates the wall clock and is the reason the transcript cache exists —
budget accordingly on a fresh `work/`, and expect a re-run to be near-instant.

The same `WHISPER_*` environment variables `phansora-api` reads are honoured here
(`WHISPER_MODEL`, `WHISPER_DEVICE`, `WHISPER_COMPUTE_TYPE`, `WHISPER_BEAM_SIZE`,
`WHISPER_LANGUAGE`, `WHISPER_VAD_FILTER`), so whatever is configured in prod carries over.

VAD is **off** by default here, deliberately — it can silently drop quiet speech, which
this tool would then report as missing content.

---

## Flags worth knowing

```
--check                    resolve everything and exit without doing work
--whole-document           measure against every page, contents and appendix included
--verbatim-shingle N       word-run length that counts as lifted (default 8)
--force-ocr                redo OCR even if work/ocr.json exists
--force-transcribe         redo Whisper even if transcripts are cached
```

**Source text**

```
--source-text FILE         a verified transcription of the PDF, bypassing OCR entirely
--ocr-gate PCT             min mean tesseract word confidence (default 85)
--lex-gate PCT             min share of lowercase tokens that are real words (default 95)
--ignore-ocr-gate          score anyway below the gates; the report carries a warning
--keep-front-matter        score copyright/title boilerplate as teaching content too
```

The lexical gate is the one that actually discriminates — tesseract's own confidence will
pass badly mangled text. If a run aborts on the gates, the source scan is bad and the
answer would be meaningless; supply `--source-text` rather than reaching for
`--ignore-ocr-gate`.

**Transcription**

```
--whisper-model medium.en  model name
--device auto|cuda|cpu
--compute-type float16     or int8
--beam-size 5
--vad / --no-vad
--language en
```

**Paths** — every default is overridable, so the same script runs unchanged against a
different tree:

```
--input-pdf FILE   --audio-dir DIR   --work-dir DIR   --out-dir DIR
```

---

## Outputs

| File | Contents |
|---|---|
| `REPORT.md` | The readable audit — the two answers, the per-lesson split, what is missing, and which pages were excluded |
| `report.json` | The same data structured: `reworded_percent`, `present_percent`, every claim with its status, and the excluded pages |
| `work/` | Caches: page renders, `ocr.json`, per-lesson transcripts |

`work/` is gitignored; the two report files are not.

Coverage percentages come from sentence-embedding similarity plus entity and number
grounding against the parsed source statements. They measure *this parse*, not ground
truth — `REPORT.md` says so in its own footer, and it is worth believing.

---

*This repo also used to hold solo voice-clone tests for three TTS engines (`neutts/`,
`cosyvoice2/`, `soprotts/`). They were dropped once the audit harness became the point of
it; `git log` still has them.*
