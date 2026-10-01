#!/usr/bin/env bash
# Compatibility entry point; verification commands now come from projects.json.
# Use --list to inspect coverage, --project NAME to select a suite, --include-gpu for CUDA.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${SCRIPT_DIR}/verify_portfolio.py" "$@"
