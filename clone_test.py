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
import re
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
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
# Use the GPU when available (prod), fall back to CPU (dev). Override with NEUTTS_DEVICE.
DEVICE = os.environ.get("NEUTTS_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")
# NeuTTS Air is short-form: the whole prompt (ref codes + ref text + input) plus the generated
# audio codes must fit the backbone's 2048-token context. Long input is split into <=MAX_CHARS
# sentence chunks, each synthesized separately and concatenated.
MAX_CHARS = int(os.environ.get("NEUTTS_MAX_CHARS", "200"))
SAMPLE_RATE = 24000


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


def chunk_text(text: str, max_chars: int) -> list[str]:
    """Pack whole sentences into chunks no longer than ``max_chars`` (never splits a sentence)."""
    chunks: list[str] = []
    buf = ""
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):
        sentence = sentence.strip()
        if not sentence:
            continue
        if not buf:
            buf = sentence
        elif len(buf) + 1 + len(sentence) <= max_chars:
            buf = f"{buf} {sentence}"
        else:
            chunks.append(buf)
            buf = sentence
    if buf:
        chunks.append(buf)
    return chunks


def main() -> None:
    ref_text = ensure_ref_text()
    # Collapse the paragraph whitespace in test.txt into a single passage for synthesis.
    input_text = " ".join(INPUT_TXT.read_text().split())

    print(f"[tts] loading NeuTTS  backbone={BACKBONE}  codec={CODEC}  device={DEVICE} ...")
    tts = NeuTTS(
        backbone_repo=BACKBONE,
        backbone_device=DEVICE,
        codec_repo=CODEC,
        codec_device=DEVICE,
    )

    print(f"[tts] encoding reference clip {REF_WAV.name} ...")
    ref_codes = tts.encode_reference(str(REF_WAV))

    chunks = chunk_text(input_text, MAX_CHARS)
    print(f"[tts] synthesizing {len(input_text)} chars from {INPUT_TXT.name} "
          f"in {len(chunks)} chunk(s) on {DEVICE}...")
    silence = np.zeros(int(0.3 * SAMPLE_RATE), dtype=np.float32)
    parts: list[np.ndarray] = []
    for i, chunk in enumerate(chunks, start=1):
        print(f"[tts]   chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        part = np.asarray(tts.infer(chunk, ref_codes, ref_text), dtype=np.float32)
        parts.append(part)
        if i < len(chunks):
            parts.append(silence)

    wav = np.concatenate(parts) if parts else np.zeros(0, dtype=np.float32)
    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(OUT_WAV), wav, SAMPLE_RATE)
    print(f"[done] wrote {OUT_WAV.relative_to(ROOT)}  ({len(wav) / SAMPLE_RATE:.1f}s)")


if __name__ == "__main__":
    main()
