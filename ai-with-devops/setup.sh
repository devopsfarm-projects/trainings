#!/usr/bin/env bash
set -euo pipefail

echo "[ai-with-devops] Environment bootstrap & checks"

fail() { echo "ERROR: $*" >&2; exit 1; }

command -v git >/dev/null || fail "git is required"
command -v python3 >/dev/null || fail "python3 is required"
command -v node >/dev/null || echo "warning: node not found — some labs require Node.js"
command -v docker >/dev/null || echo "warning: docker not found — some labs use Docker"

PYVENV=.venv
if [ ! -d "$PYVENV" ]; then
  echo "Creating Python venv at $PYVENV"
  python3 -m venv "$PYVENV"
fi

echo "Activating venv and installing python deps (if requirements.txt present)"
source "$PYVENV/bin/activate"
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "No requirements.txt found — skipping pip install"
fi

echo "Done. Remember to provide API keys using environment variables or your CI provider's secrets. See secrets.example"
