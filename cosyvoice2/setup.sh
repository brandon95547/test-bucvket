#!/usr/bin/env bash
# One-time setup for the CosyVoice 2 clone test. CosyVoice is not pip-installable and
# needs Python 3.10, so this:
#   1. clones the CosyVoice repo (+ Matcha-TTS submodule)
#   2. creates a Python 3.10 .venv and installs deps (CosyVoice's pins + our extras)
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

echo "== 3/4 install deps =="
# openai-whisper==20231117 (a CosyVoice pin) has a legacy setup.py that imports
# pkg_resources at build time; setuptools>=81 no longer ships it, so pip's *isolated*
# build env fails with "No module named 'pkg_resources'". Pin an older setuptools in the
# venv and build whisper WITHOUT build isolation so it uses that. Do this before the
# requirements install so the pinned whisper is already satisfied.
.venv/bin/pip install "setuptools<81" wheel
.venv/bin/pip install --no-build-isolation openai-whisper==20231117
# CosyVoice's own pinned requirements (torch==2.3.1+cu121, transformers, onnxruntime, ...),
# then this test's extras.
.venv/bin/pip install -r CosyVoice/requirements.txt
.venv/bin/pip install -r requirements.txt

echo "== 4/4 download CosyVoice2-0.5B (~2 GB) =="
.venv/bin/python - <<'PY'
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice2-0.5B',
                  local_dir='CosyVoice/pretrained_models/CosyVoice2-0.5B')
PY

echo "Done. Run:  .venv/bin/python clone_test.py"
