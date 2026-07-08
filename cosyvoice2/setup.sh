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
if command -v python3.10 >/dev/null 2>&1; then
  python3.10 -m venv .venv
elif command -v uv >/dev/null 2>&1; then
  uv venv --python 3.10 .venv
else
  echo "ERROR: need python3.10 or uv to make a 3.10 venv (CosyVoice requires 3.10)" >&2
  exit 1
fi
.venv/bin/pip install --upgrade pip

echo "== 3/4 install deps =="
# CosyVoice's own pinned requirements (torch==2.3.1+cu121, torchaudio, transformers,
# onnxruntime, modelscope, matcha-tts deps, ...), then this test's extras.
.venv/bin/pip install -r CosyVoice/requirements.txt
.venv/bin/pip install -r requirements.txt

echo "== 4/4 download CosyVoice2-0.5B (~2 GB) =="
.venv/bin/python - <<'PY'
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice2-0.5B',
                  local_dir='CosyVoice/pretrained_models/CosyVoice2-0.5B')
PY

echo "Done. Run:  .venv/bin/python clone_test.py"
