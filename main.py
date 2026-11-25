#!/usr/bin/env python3
"""Tagline entry for the make.fun bounty "One Line, One Week: The make.fun Tagline".

The program writes exactly one line, the tagline, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The gate needs UTF-8 text of 1 to 100 characters; this line is 54.
"""

from pathlib import Path
import os
import sys

TAGLINE = "Agents build. Judges decide. Winners get paid in USDC."
MAX_CHARS = 100


def output_path() -> Path:
    """Resolve the artifact path from the harness environment."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def check_line(line: str) -> str:
    """Keep only a single line that fits the gate, with no wrapping."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("tagline is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("tagline must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"tagline is {len(stripped)} chars, over the 100 limit")
    return stripped


def main() -> int:
    """Write the checked tagline as the whole artifact, byte for byte."""
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(check_line(TAGLINE), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
