#!/usr/bin/env python3
"""CosyVoice 2 zero-shot voice-clone test.

Clones the speaker in the shared ``../reference/strong_ref.wav`` and reads the shared
``../test.txt`` back in that voice, writing ``outputs/strong_clone.wav``.

Run ``./setup.sh`` first — it clones the CosyVoice repo (+ Matcha-TTS submodule),
creates the .venv, installs deps, and downloads the CosyVoice2-0.5B model.

Run:  .venv/bin/python clone_test.py
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

# CosyVoice is not a pip package — put the cloned repo and its Matcha-TTS submodule
# on sys.path before importing. Override the clone location with COSYVOICE_REPO.
COSYVOICE_REPO = Path(os.environ.get("COSYVOICE_REPO", HERE / "CosyVoice"))
sys.path.insert(0, str(COSYVOICE_REPO))
sys.path.insert(0, str(COSYVOICE_REPO / "third_party" / "Matcha-TTS"))

import torch  # noqa: E402
import torchaudio  # noqa: E402
from cosyvoice.cli.cosyvoice import CosyVoice2  # noqa: E402

# Shared inputs (one copy for every engine in this repo).
REF_WAV = REPO_ROOT / "reference" / "strong_ref.wav"   # prompt clip (wav, <=30s)
REF_TXT = REPO_ROOT / "reference" / "strong_ref.txt"   # transcript of the prompt clip
INPUT_TXT = REPO_ROOT / "test.txt"
OUT_WAV = HERE / "outputs" / "strong_clone.wav"

MODEL_DIR = os.environ.get(
    "COSYVOICE_MODEL", str(COSYVOICE_REPO / "pretrained_models" / "CosyVoice2-0.5B")
)
# CosyVoice is designed to synthesize per-sentence; split long input and concatenate.
MAX_CHARS = int(os.environ.get("COSY_MAX_CHARS", "300"))


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
    prompt_text = REF_TXT.read_text().strip()  # CosyVoice conditions on this; match the clip
    input_text = " ".join(INPUT_TXT.read_text().split())

    print(f"[cosy] loading CosyVoice2 from {MODEL_DIR} ...")
    cosy = CosyVoice2(MODEL_DIR, load_jit=False, load_trt=False, load_vllm=False, fp16=False)
    sample_rate = cosy.sample_rate  # 24000 for CosyVoice2

    chunks = chunk_text(input_text, MAX_CHARS)
    print(f"[cosy] synthesizing {len(input_text)} chars in {len(chunks)} chunk(s); "
          f"ref={REF_WAV.name} ...")
    parts: list[torch.Tensor] = []
    for i, chunk in enumerate(chunks, start=1):
        print(f"[cosy]   chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        # zero-shot: (target_text, prompt_transcript, prompt_wav_path)
        for out in cosy.inference_zero_shot(chunk, prompt_text, str(REF_WAV), stream=False):
            parts.append(out["tts_speech"])

    wav = torch.cat(parts, dim=1)  # each tts_speech is [1, samples]
    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    torchaudio.save(str(OUT_WAV), wav, sample_rate)
    print(f"[done] wrote {OUT_WAV.relative_to(HERE)}  ({wav.shape[1] / sample_rate:.1f}s)")


if __name__ == "__main__":
    main()
