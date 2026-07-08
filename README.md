# test-bucvket — TTS voice-clone test harness

Solo clone tests for three TTS engines, all against the **same shared inputs** so their output
can be compared apples-to-apples:

- **Reference voice:** `reference/strong_ref.wav` (+ transcript `reference/strong_ref.txt`)
- **Input text:** `test.txt`

Each engine lives in its **own folder** with its own `requirements.txt`/setup, script, and
`.venv` — set up and test **one engine at a time**, and delete that engine's `.venv` (and any
cloned repo/model) when you switch. Nothing bleeds between engines.

| Engine | Folder | Setup | Run |
|---|---|---|---|
| NeuTTS Air | `neutts/` | `pip install -r requirements.txt` | `.venv/bin/python clone_test.py` |
| CosyVoice 2 | `cosyvoice2/` | `./setup.sh` (repo clone + ~2 GB model) | `.venv/bin/python clone_test.py` |
| SoproTTS | `soprotts/` | `pip install -r requirements.txt` | `.venv/bin/python clone_test.py` |

Each engine reads the shared inputs via `../reference/…` and `../test.txt`, and writes
`outputs/strong_clone.wav` in its own folder. See each folder's `README.md` for specifics.

## Typical flow (one engine at a time)
```bash
cd neutts
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python clone_test.py
rm -rf .venv        # reclaim space before switching engines
```

`.venv/`, `outputs/`, downloaded models, and cloned upstream repos are gitignored.

## Engines at a glance
- **NeuTTS Air** — needs the reference transcript; short-form (auto-chunks long text); tunable
  sampling via `NEUTTS_*` env vars.
- **CosyVoice 2** — Python 3.10, repo clone + Matcha-TTS submodule + ~2 GB model; needs the
  reference transcript.
- **SoproTTS** — smallest/fastest; English-only; true zero-shot (no transcript needed).
