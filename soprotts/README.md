# SoproTTS — voice clone test

Zero-shot voice clone with [SoproTTS](https://github.com/samuel-vitorino/sopro) — a small
(135M), English-only, CPU-fast model. Clones the shared `../reference/strong_ref.wav` and
reads `../test.txt` in that voice → `outputs/strong_clone.wav`.

Unlike NeuTTS / CosyVoice, Sopro is **true zero-shot: no reference transcript needed** — you
pass only the reference audio path and the target text.

## Setup
```bash
cd soprotts
python -m venv .venv
.venv/bin/pip install -r requirements.txt    # sopro (pulls torch/torchaudio/etc.)
```
The model downloads automatically on first run (`SoproTTS.from_pretrained`).

## Run
```bash
.venv/bin/python clone_test.py               # cuda if available, else cpu
SOPRO_DEVICE=cpu .venv/bin/python clone_test.py   # force CPU (it's fast enough)
```

## Notes
- **Reference clip:** 3–12 s recommended (the shared clip is ~13 s — Sopro handles it; trim if
  it misbehaves). WAV or MP3.
- **English only.**
- Sopro also supports `temperature`, `top_p`, and `style_strength` (FiLM strength, default 1.2)
  for voice-similarity vs. stability — not wired into this script; add if you want to tune.
