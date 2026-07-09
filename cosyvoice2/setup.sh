#!/usr/bin/env bash
# One-time setup for the CosyVoice 2 clone test. CosyVoice is not pip-installable and
# needs Python 3.10, so this:
#   1. clones the CosyVoice repo (+ Matcha-TTS submodule)
#   2. creates a Python 3.10 .venv and installs deps into ONE env — CosyVoice + vLLM +
#      TensorRT — resolved around torch 2.7 (vLLM's requirement; see step 3 for why).
#   3. downloads the CosyVoice2-0.5B model (~2 GB) into CosyVoice/pretrained_models/
#
# System deps required first:  sox libsox-dev  (dnf: sox sox-devel) and ffmpeg.
# Then:  ./setup.sh   ->   .venv/bin/python clone_test.py
set -euo pipefail
cd "$(cd "$(dirname "$0")" && pwd)"

echo "== 1/4 clone CosyVoice (+ submodules) =="
if [ ! -d CosyVoice/.git ]; then
  git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
else
  ( cd CosyVoice && git submodule update --init --recursive )
fi

echo "== 2/4 create Python 3.10 venv =="
if [ ! -d .venv ]; then
  if command -v python3.10 >/dev/null 2>&1; then
    python3.10 -m venv .venv
  elif command -v uv >/dev/null 2>&1; then
    # --seed installs pip/setuptools/wheel into the venv (uv omits them by default)
    uv venv --python 3.10 --seed .venv
  else
    echo "ERROR: need python3.10 or uv to make a 3.10 venv (CosyVoice requires 3.10)" >&2
    exit 1
  fi
fi  # reuse an existing venv on re-runs (don't re-download multi-GB torch)
.venv/bin/pip install --upgrade pip

echo "== 3/4 install deps (single env, vLLM-enabled) =="
# We install EVERYTHING into one venv, including vLLM + TensorRT, so the fast inference
# path (COSY_FAST=1) works without a second environment.
#
# The catch: vLLM 0.9.0 requires torch 2.7, but CosyVoice pins torch==2.3.1. In one env
# there is only ever one torch, so vLLM's version wins. To avoid downloading torch twice
# (2.3.1 then 2.7) and to stop CosyVoice's pin from downgrading it back, we:
#   1. install vLLM FIRST so torch resolves straight to 2.7.0, and
#   2. install CosyVoice's requirements under a CONSTRAINTS file that forbids the downgrade.
# transformers 4.51.3 and numpy 1.26.4 are what BOTH vLLM 0.9.0 and CosyVoice want, so they
# stay put. tensorrt-cu12 is already in CosyVoice/requirements.txt — no separate install.
#
# NOTE: this runs CosyVoice on torch 2.7 (upstream only tests 2.3.1). It works fine on
# Ampere (A4000) in practice, but re-listen to outputs/strong_clone.wav once to confirm
# quality held. pip may warn about a few web-serving pins (fastapi/pydantic/gradio) that
# vLLM bumps — those are irrelevant to inference and safe to ignore.

# openai-whisper==20231117 (a CosyVoice pin) has a legacy setup.py that imports
# pkg_resources at build time; setuptools>=81 no longer ships it, so pip's *isolated*
# build env fails with "No module named 'pkg_resources'". Pin an older setuptools and build
# whisper WITHOUT build isolation so it uses that.
.venv/bin/pip install "setuptools<81" wheel

# 1. vLLM first — pulls torch==2.7.0 exactly once. Pin torchaudio to match (import fails
#    otherwise). transformers/numpy pinned to the values CosyVoice also needs.
.venv/bin/pip install vllm==0.9.0 torchaudio==2.7.0 transformers==4.51.3 numpy==1.26.4

# whisper now that torch is present (no-build-isolation avoids the pkg_resources failure).
.venv/bin/pip install --no-build-isolation openai-whisper==20231117

# 2. Install CosyVoice's requirements, but STRIP its torch/torchaudio pins first. A pip
#    constraints file can't override an explicit '==' pin — pip treats "requirements wants
#    torch==2.3.1" + "constraint wants torch==2.7.0" as a hard conflict (ResolutionImpossible).
#    So we delete those two lines and let the already-installed torch 2.7.0 satisfy the
#    (loose) torch deps of everything else. transformers==4.51.3 / numpy==1.26.4 stay in the
#    file and already match what we installed, so they resolve cleanly. Everything else
#    (tensorrt-cu12, onnxruntime-gpu, conformer, matcha deps, ...) installs normally.
sed -E '/^(torch|torchaudio)==/d' CosyVoice/requirements.txt > /tmp/cosy_reqs.txt
.venv/bin/pip install -r /tmp/cosy_reqs.txt

# 3. This test's extras (modelscope, soundfile).
.venv/bin/pip install -r requirements.txt

echo "== 4/4 download CosyVoice2-0.5B (~2 GB) =="
.venv/bin/python - <<'PY'
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice2-0.5B',
                  local_dir='CosyVoice/pretrained_models/CosyVoice2-0.5B')
PY

echo "Done."
echo "  baseline (fp16 + cached speaker):  .venv/bin/python clone_test.py"
echo "  fast path (vLLM + TensorRT):       COSY_FAST=1 .venv/bin/python clone_test.py"
echo "  (run the fast path TWICE — the first run exports the vLLM/TRT engines.)"
