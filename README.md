# NeuTTS Air — voice clone test

A minimal [NeuTTS Air](https://github.com/neuphonic/neutts-air) voice-cloning smoke test.
It clones the speaker in a reference clip and reads `test.txt` back in that voice.

- **Reference voice:** `reference/strong_ref.wav` — the first 15s of `strong.mp3`, mono/24 kHz
  (NeuTTS wants a 3–15s clip).
- **Reference transcript:** `reference/strong_ref.txt` — NeuTTS conditions on the reference
  audio **and** its transcript. It's auto-generated from the clip with `faster-whisper` on the
  first run; **review/hand-correct it** for a cleaner clone.
- **Input text:** `test.txt`.
- **Output:** `outputs/strong_clone.wav` (24 kHz).

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install --index-url https://download.pytorch.org/whl/cpu torch torchaudio
.venv/bin/pip install -r requirements.txt   # neutts, soundfile, faster-whisper
# system deps: espeak-ng + ffmpeg must be installed
```

## Run

```bash
.venv/bin/python clone_test.py
```

First run downloads the models (`neuphonic/neutts-air`, `neuphonic/neucodec`, whisper `base`)
and runs on **CPU**, so it is slow. Options via env:

```bash
NEUTTS_BACKBONE=neuphonic/neutts-nano .venv/bin/python clone_test.py   # smaller/faster backbone
```

## Notes

- NeuTTS Air is short-form (2048-token context: ref audio + ref text + input + generated audio).
  The script auto-splits input into `NEUTTS_MAX_CHARS`-sized sentence chunks (default 200) and
  concatenates the results, so long passages like `test.txt` work. If a single long sentence still
  overflows, lower `NEUTTS_MAX_CHARS` or shorten `reference/strong_ref.wav`.
- To re-transcribe the reference, delete `reference/strong_ref.txt` and re-run.
