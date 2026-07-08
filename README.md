# test-bucvket — TTS voice-clone test harness

Solo clone tests for several TTS engines, all against the **same shared inputs** so their
output can be compared apples-to-apples:

- **Reference voice:** `reference/strong_ref.wav` (+ its transcript `reference/strong_ref.txt`)
- **Input text:** `test.txt`

Each engine lives in its own directory with its **own `requirements.txt`, script, and `.venv`**,
so you set up and test **one engine at a time** — and can delete that engine's `.venv` (and any
cloned repo/model) when you switch. Nothing bleeds between engines.

| Engine | Dir | Setup | Run | Notes |
|---|---|---|---|---|
| NeuTTS Air | `./` (root) — [docs](neutts.md) | `pip install -r requirements.txt` | `.venv/bin/python clone_test.py` | small, CPU-ok |
| CosyVoice 2 | `cosyvoice2/` | `./setup.sh` | `.venv/bin/python clone_test.py` | py3.10, repo clone + ~2 GB model |
| SoproTTS | `soprotts/` | _(coming)_ | | |

Each engine writes `outputs/strong_clone.wav`. `.venv/`, `outputs/`, downloaded models, and
cloned upstream repos are gitignored.

## Switching engines
```bash
# example: test CosyVoice 2, then reclaim space before switching
cd cosyvoice2 && ./setup.sh && .venv/bin/python clone_test.py
rm -rf .venv CosyVoice          # free disk when done with this engine
```

The reference clip and `test.txt` are shared at the repo root; each engine's script reads them
via `../reference/…` and `../test.txt` (the root NeuTTS script reads them in place).
