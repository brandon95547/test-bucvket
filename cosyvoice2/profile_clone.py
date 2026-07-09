#!/usr/bin/env python3
"""Stage-level profiler for the CosyVoice2 zero-shot pipeline.

Confirms *where* the 72s goes on your A4000: prompt/frontend extraction (CPU/ONNX),
LLM autoregressive token generation (GPU, batch-1), and flow+hift token->wav (GPU).
It monkeypatches the three hot methods to accumulate wall time + a CUDA-synced GPU
timer, and counts LLM decode steps so you get ms/token.

Run:  .venv/bin/python profile_clone.py
Env:  same as clone_test.py (COSYVOICE_REPO, COSYVOICE_MODEL, COSY_MAX_CHARS).
"""
from __future__ import annotations
import os, re, sys, time, contextlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
COSYVOICE_REPO = Path(os.environ.get("COSYVOICE_REPO", HERE / "CosyVoice"))
sys.path.insert(0, str(COSYVOICE_REPO))
sys.path.insert(0, str(COSYVOICE_REPO / "third_party" / "Matcha-TTS"))

import torch  # noqa: E402
import torchaudio  # noqa: E402
from cosyvoice.cli.cosyvoice import CosyVoice2  # noqa: E402
from cosyvoice.cli import frontend as fe_mod  # noqa: E402
from cosyvoice.cli import model as model_mod  # noqa: E402

REF_WAV = REPO_ROOT / "reference" / "strong_ref.wav"
REF_TXT = REPO_ROOT / "reference" / "strong_ref.txt"
INPUT_TXT = REPO_ROOT / "test.txt"
OUT_WAV = HERE / "outputs" / "profile_clone.wav"
MODEL_DIR = os.environ.get("COSYVOICE_MODEL", str(COSYVOICE_REPO / "pretrained_models" / "CosyVoice2-0.5B"))
MAX_CHARS = int(os.environ.get("COSY_MAX_CHARS", "300"))

CUDA = torch.cuda.is_available()
stats = {"llm_job": [0.0, 0], "token2wav": [0.0, 0], "extract_token": [0.0, 0],
         "extract_spk": [0.0, 0], "extract_feat": [0.0, 0], "llm_steps": [0]}


@contextlib.contextmanager
def timed(key, count_key=None):
    if CUDA:
        torch.cuda.synchronize()
    t0 = time.perf_counter()
    yield
    if CUDA:
        torch.cuda.synchronize()
    stats[key][0] += time.perf_counter() - t0
    stats[key][1] += 1


def wrap(obj, name, key):
    orig = getattr(obj, name)
    def w(*a, **k):
        with timed(key):
            return orig(*a, **k)
    setattr(obj, name, w)


def chunk_text(text, max_chars):
    chunks, buf = [], ""
    for s in re.split(r"(?<=[.!?])\s+", text.strip()):
        s = s.strip()
        if not s:
            continue
        if not buf:
            buf = s
        elif len(buf) + 1 + len(s) <= max_chars:
            buf = f"{buf} {s}"
        else:
            chunks.append(buf); buf = s
    if buf:
        chunks.append(buf)
    return chunks


def main():
    prompt_text = REF_TXT.read_text().strip()
    input_text = " ".join(INPUT_TXT.read_text().split())

    cosy = CosyVoice2(MODEL_DIR, load_jit=False, load_trt=False, load_vllm=False, fp16=False)
    sr = cosy.sample_rate

    # Patch frontend prompt extraction (CPU/ONNX) and model GPU stages.
    fe = cosy.frontend
    wrap(fe, "_extract_speech_token", "extract_token")
    wrap(fe, "_extract_spk_embedding", "extract_spk")
    wrap(fe, "_extract_speech_feat", "extract_feat")
    wrap(cosy.model, "token2wav", "token2wav")

    # Count LLM decode steps + time the whole llm_job thread body.
    orig_llm_job = cosy.model.llm_job
    def llm_job(*a, **k):
        with timed("llm_job"):
            return orig_llm_job(*a, **k)
    cosy.model.llm_job = llm_job
    orig_fos = cosy.model.llm.llm.forward_one_step
    def fos(*a, **k):
        stats["llm_steps"][0] += 1
        return orig_fos(*a, **k)
    cosy.model.llm.llm.forward_one_step = fos

    chunks = chunk_text(input_text, MAX_CHARS)
    print(f"[profile] {len(input_text)} chars -> {len(chunks)} chunk(s), fp16=False, vllm/trt/jit off")
    wall0 = time.perf_counter()
    parts = []
    for i, chunk in enumerate(chunks, 1):
        for out in cosy.inference_zero_shot(chunk, prompt_text, str(REF_WAV), stream=False):
            parts.append(out["tts_speech"])
    wall = time.perf_counter() - wall0

    wav = torch.cat(parts, dim=1)
    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    torchaudio.save(str(OUT_WAV), wav, sr)
    audio_s = wav.shape[1] / sr

    steps = stats["llm_steps"][0]
    llm_t = stats["llm_job"][0]
    print("\n==== stage breakdown (wall seconds) ====")
    print(f"  total wall .............. {wall:8.2f}s   audio={audio_s:.1f}s   RTF={wall/audio_s:.3f}")
    print(f"  LLM autoregressive ...... {llm_t:8.2f}s   ({100*llm_t/wall:4.1f}%)  steps={steps}  "
          f"{1000*llm_t/max(steps,1):.1f} ms/token")
    print(f"  flow+hift token2wav ..... {stats['token2wav'][0]:8.2f}s   ({100*stats['token2wav'][0]/wall:4.1f}%)  calls={stats['token2wav'][1]}")
    print(f"  prompt speech_token(ONNX) {stats['extract_token'][0]:8.2f}s   ({100*stats['extract_token'][0]/wall:4.1f}%)  calls={stats['extract_token'][1]}")
    print(f"  prompt spk_emb (campplus) {stats['extract_spk'][0]:8.2f}s   ({100*stats['extract_spk'][0]/wall:4.1f}%)  calls={stats['extract_spk'][1]}")
    print(f"  prompt speech_feat ...... {stats['extract_feat'][0]:8.2f}s   ({100*stats['extract_feat'][0]/wall:4.1f}%)  calls={stats['extract_feat'][1]}")
    if CUDA:
        print(f"  peak VRAM ............... {torch.cuda.max_memory_allocated()/1e9:.2f} GB")
    print("\nNote: prompt extraction calls > 1 means the same reference is re-processed per "
          "sentence — cache it with add_zero_shot_spk (see report).")


if __name__ == "__main__":
    main()
