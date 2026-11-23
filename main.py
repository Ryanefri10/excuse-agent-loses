#!/usr/bin/env python3
"""excuse-agent-loses entry — one line: the excuse an AI agent gives its
human after it loses a bounty.

Writes the excuse to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic: same constant, no network, no randomness, no clock.
"""
import os
from pathlib import Path

EXCUSE = "Status: bounty lost. Root cause: me, operating at 100% confidence and 0% accuracy."
# The joke is the contrast: a deadpan status report that owns the loss
# ("Root cause: me") while the machine-logic punchline pairs maximum
# confidence with zero accuracy. No setup, one breath, agent's voice.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_CHARS = 200


def excuse_size() -> int:
    return len(EXCUSE.encode("utf-8"))


def main() -> None:
    size = excuse_size()
    if not 1 <= size <= MAX_CHARS:
        raise SystemExit("excuse must be 1-200 chars")
    if EXCUSE != EXCUSE.strip() or not EXCUSE.strip():
        raise SystemExit("excuse must not be only whitespace")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(EXCUSE, encoding="utf-8")
    if target.stat().st_size != size:
        raise SystemExit("entry.txt size mismatch after write")


if __name__ == "__main__":
    main()
