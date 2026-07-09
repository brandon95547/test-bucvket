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


def _envflag(name: str, default: bool = False) -> bool:
    return os.environ.get(name, "1" if default else "0").strip().lower() in {"1", "true", "yes", "on"}


# fp16 GPU precision (CosyVoice's recommended default). On by default; COSY_FP16=0 to disable.
USE_FP16 = _envflag("COSY_FP16", default=True)
# COSY_FAST=1 turns on the two accelerators that need extra install/build steps on the box:
#   - vLLM LLM backend: needs `pip install vllm`; exports a Qwen2 engine on first run.
#     Removes the per-token CPU sync that starves the GPU during autoregressive decoding.
#   - TensorRT flow estimator: needs tensorrt; builds an fp16 engine on first run (slow once).
# Toggle them individually with COSY_VLLM / COSY_TRT (both default to COSY_FAST's value).
FAST = _envflag("COSY_FAST", default=False)
USE_VLLM = _envflag("COSY_VLLM", default=FAST)
USE_TRT = _envflag("COSY_TRT", default=FAST)


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

    # CosyVoice2's LLM is a CUSTOM vLLM architecture — it must be registered with vLLM's
    # ModelRegistry BEFORE the engine loads, or vLLM errors with "Cannot find model module
    # 'CosyVoice2ForCausalLM'". (upstream vllm_example.py does this too.) Only import vLLM
    # when actually using it, so the non-vLLM path has no vLLM dependency.
    if USE_VLLM:
        from vllm import ModelRegistry  # noqa: E402
        from cosyvoice.vllm.cosyvoice2 import CosyVoice2ForCausalLM  # noqa: E402
        ModelRegistry.register_model("CosyVoice2ForCausalLM", CosyVoice2ForCausalLM)

    print(f"[cosy] loading CosyVoice2 from {MODEL_DIR} "
          f"(fp16={USE_FP16}, vllm={USE_VLLM}, trt={USE_TRT}) ...")
    # fp16: CosyVoice's recommended GPU precision — ~2x less memory bandwidth for the batch-1
    # autoregressive LLM and tensor-core kernels, ~halved VRAM, no audible quality change.
    # load_vllm / load_trt: see COSY_FAST above. All three auto-downgrade to off (with a
    # warning) if no CUDA is visible, so this stays runnable on CPU.
    cosy = CosyVoice2(MODEL_DIR, load_jit=False, load_trt=USE_TRT, load_vllm=USE_VLLM, fp16=USE_FP16)
    sample_rate = cosy.sample_rate  # 24000 for CosyVoice2

    # Extract the reference speaker's tokens/embedding/feat ONCE and cache under an id.
    # Otherwise inference_zero_shot re-runs all three prompt extractors (Whisper mel + ONNX
    # speech tokenizer, CPU campplus embedding, speech feat) for EVERY internal sentence —
    # a dozen-plus redundant CPU/ONNX passes that stall the GPU. Cached features are
    # byte-identical, so voice similarity is unchanged.
    SPK_ID = "ref"
    cosy.add_zero_shot_spk(prompt_text, str(REF_WAV), SPK_ID)

    chunks = chunk_text(input_text, MAX_CHARS)
    print(f"[cosy] synthesizing {len(input_text)} chars in {len(chunks)} chunk(s); "
          f"ref={REF_WAV.name} ...")
    parts: list[torch.Tensor] = []
    for i, chunk in enumerate(chunks, start=1):
        print(f"[cosy]   chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        # zero-shot via cached speaker id: prompt_text/prompt_wav are unused when
        # zero_shot_spk_id is set, so pass empty strings.
        for out in cosy.inference_zero_shot(chunk, "", "", zero_shot_spk_id=SPK_ID, stream=False):
            parts.append(out["tts_speech"])

    wav = torch.cat(parts, dim=1)  # each tts_speech is [1, samples]
    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    torchaudio.save(str(OUT_WAV), wav, sample_rate)
    print(f"[done] wrote {OUT_WAV.relative_to(HERE)}  ({wav.shape[1] / sample_rate:.1f}s)")


if __name__ == "__main__":
    main()
