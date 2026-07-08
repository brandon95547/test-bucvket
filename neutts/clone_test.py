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

ROOT = Path(__file__).resolve().parent      # this engine's dir (neutts/)
REPO_ROOT = ROOT.parent                      # shared inputs live at the repo root
REF_WAV = REPO_ROOT / "reference" / "strong_ref.wav"   # shared reference clip
REF_TXT = REPO_ROOT / "reference" / "strong_ref.txt"   # shared reference transcript
INPUT_TXT = REPO_ROOT / "test.txt"                     # shared input text
OUT_WAV = ROOT / "outputs" / "strong_clone.wav"        # per-engine output

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

# Generation sampling. NeuTTS's built-in generate() uses temperature=1.0 with NO
# repetition_penalty (neutts/neutts.py), which makes a small AR model repeat words and
# drift in pace. We wrap the backbone's generate() to inject steadier defaults; all
# env-tunable so you can dial them in by ear.
GEN_TEMPERATURE = float(os.environ.get("NEUTTS_TEMPERATURE", "0.8"))
GEN_REPETITION_PENALTY = float(os.environ.get("NEUTTS_REPETITION_PENALTY", "1.1"))
GEN_TOP_P = float(os.environ.get("NEUTTS_TOP_P", "0.9"))


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


def _tune_generation(tts: NeuTTS) -> None:
    """Override NeuTTS's hardcoded sampling to curb word repetition / unsteady pacing.

    The library calls ``backbone.generate(temperature=1.0, top_k=50, ...)`` with no
    repetition_penalty. We wrap it to add a repetition penalty, lower the temperature,
    and use nucleus (top_p) sampling. Only affects the torch backbone (not GGUF).
    """
    backbone = getattr(tts, "backbone", None)
    if backbone is None or not callable(getattr(backbone, "generate", None)):
        print("[tts] generation tuning skipped (no torch backbone — GGUF path?)")
        return
    _orig_generate = backbone.generate

    def generate(*args, **kwargs):
        kwargs["temperature"] = GEN_TEMPERATURE
        kwargs["repetition_penalty"] = GEN_REPETITION_PENALTY
        kwargs["top_p"] = GEN_TOP_P
        return _orig_generate(*args, **kwargs)

    backbone.generate = generate
    print(f"[tts] generation tuned: temperature={GEN_TEMPERATURE} "
          f"repetition_penalty={GEN_REPETITION_PENALTY} top_p={GEN_TOP_P}")


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
    _tune_generation(tts)

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
