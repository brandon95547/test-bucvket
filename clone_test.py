#!/usr/bin/env python3
"""Basic NeuTTS Air voice-clone test.

Clones the speaker in ``reference/strong_ref.wav`` and reads ``test.txt`` back in
that voice, writing ``outputs/strong_clone.wav``.

NeuTTS needs the *transcript* of the reference clip (it conditions on ref audio +
ref text). If ``reference/strong_ref.txt`` is missing we auto-generate it from the
clip with faster-whisper — review/hand-correct that file for a better clone.

Run:  .venv/bin/python clone_test.py
"""
from __future__ import annotations

import os
from pathlib import Path

import soundfile as sf
from neutts import NeuTTS

ROOT = Path(__file__).resolve().parent
REF_WAV = ROOT / "reference" / "strong_ref.wav"
REF_TXT = ROOT / "reference" / "strong_ref.txt"
INPUT_TXT = ROOT / "test.txt"
OUT_WAV = ROOT / "outputs" / "strong_clone.wav"

# neuphonic/neutts-air is the flagship; override with NEUTTS_BACKBONE (e.g. neutts-nano
# for a faster CPU run, or a *-gguf repo if you install llama-cpp-python).
BACKBONE = os.environ.get("NEUTTS_BACKBONE", "neuphonic/neutts-air")
CODEC = os.environ.get("NEUTTS_CODEC", "neuphonic/neucodec")


def ensure_ref_text() -> str:
    """Return the reference transcript, transcribing the clip if we don't have one."""
    if REF_TXT.exists() and REF_TXT.read_text().strip():
        return REF_TXT.read_text().strip()

    print(f"[ref] no transcript at {REF_TXT.name}; transcribing {REF_WAV.name} with faster-whisper...")
    from faster_whisper import WhisperModel

    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(REF_WAV))
    text = " ".join(s.text.strip() for s in segments).strip()
    REF_TXT.write_text(text + "\n")
    print(f"[ref] transcript saved to {REF_TXT.name}:\n      {text!r}")
    return text


def main() -> None:
    ref_text = ensure_ref_text()
    # Collapse the paragraph whitespace in test.txt into a single passage for synthesis.
    input_text = " ".join(INPUT_TXT.read_text().split())

    print(f"[tts] loading NeuTTS  backbone={BACKBONE}  codec={CODEC}  (cpu)...")
    tts = NeuTTS(
        backbone_repo=BACKBONE,
        backbone_device="cpu",
        codec_repo=CODEC,
        codec_device="cpu",
    )

    print(f"[tts] encoding reference clip {REF_WAV.name} ...")
    ref_codes = tts.encode_reference(str(REF_WAV))

    print(f"[tts] synthesizing {len(input_text)} chars from {INPUT_TXT.name} (CPU — this can take a while)...")
    wav = tts.infer(input_text, ref_codes, ref_text)

    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(OUT_WAV), wav, 24000)
    print(f"[done] wrote {OUT_WAV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
