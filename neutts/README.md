# NeuTTS Air — voice clone test (root engine)

A minimal [NeuTTS Air](https://github.com/neuphonic/neutts-air) voice-cloning smoke test.
Clones the speaker in the shared reference clip and reads `test.txt` back in that voice.
(This engine lives at the repo root; `clone_test.py`, `requirements.txt`, and `.venv` are here.)

- **Reference voice:** `reference/strong_ref.wav` (shared). NeuTTS resamples to 16 kHz mono internally.
- **Reference transcript:** `reference/strong_ref.txt` — NeuTTS conditions on the reference audio
  **and** its transcript, so it should match the clip. Auto-generated with `faster-whisper` if missing.
- **Input text:** `test.txt`.
- **Output:** `outputs/strong_clone.wav` (24 kHz).

## Setup
```bash
python3 -m venv .venv
# CPU box: --index-url https://download.pytorch.org/whl/cpu ; GPU box: .../whl/cu126
.venv/bin/pip install torch torchaudio
.venv/bin/pip install -r requirements.txt   # neutts, soundfile, faster-whisper
# system deps: espeak-ng + ffmpeg
```

## Run
```bash
.venv/bin/python clone_test.py               # auto-uses CUDA if available, else CPU
```

## Notes
- **Length:** NeuTTS Air is short-form (2048-token context = ref audio + ref text + input +
  generated audio). The script splits input into `NEUTTS_MAX_CHARS` (default 200) sentence chunks
  and concatenates. If a single long sentence overflows, lower `NEUTTS_MAX_CHARS` or shorten the ref.
- **Generation tuning** (to curb word-repeats / unsteady pacing — all env-overridable):
  `NEUTTS_TEMPERATURE` (default 0.8), `NEUTTS_REPETITION_PENALTY` (default 1.1),
  `NEUTTS_TOP_P` (default 0.9). Sweet spot is roughly temp 0.65–0.75, penalty 1.0–1.1.
- To re-transcribe the reference, delete `reference/strong_ref.txt` and re-run.
