#!/usr/bin/env python3
"""SoproTTS zero-shot voice-clone test.

Clones the speaker in the shared ``../reference/strong_ref.wav`` and reads the shared
``../test.txt`` back in that voice, writing ``outputs/strong_clone.wav``.

SoproTTS is English-only, small (135M), CPU-fast, and **true zero-shot — no reference
transcript is needed** (unlike NeuTTS / CosyVoice).

Setup:  python -m venv .venv && .venv/bin/pip install -r requirements.txt
Run:    .venv/bin/python clone_test.py
"""
from __future__ import annotations

import os
from pathlib import Path

import torch
from sopro import SoproTTS

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

# Shared inputs (one copy for every engine in this repo).
REF_WAV = REPO_ROOT / "reference" / "strong_ref.wav"   # 3-12s clip; NO transcript needed
INPUT_TXT = REPO_ROOT / "test.txt"
OUT_WAV = HERE / "outputs" / "strong_clone.wav"

MODEL = os.environ.get("SOPRO_MODEL", "samuel-vitorino/sopro")
DEVICE = os.environ.get("SOPRO_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")


def main() -> None:
    input_text = " ".join(INPUT_TXT.read_text().split())

    print(f"[sopro] loading {MODEL} on {DEVICE} ...")
    tts = SoproTTS.from_pretrained(MODEL, device=DEVICE)

    print(f"[sopro] synthesizing {len(input_text)} chars; ref={REF_WAV.name} ...")
    wav = tts.synthesize(input_text, ref_audio_path=str(REF_WAV))

    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    tts.save_wav(str(OUT_WAV), wav)
    print(f"[done] wrote {OUT_WAV.relative_to(HERE)}")


if __name__ == "__main__":
    main()
