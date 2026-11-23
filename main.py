#!/usr/bin/env python3
"""Write this make.fun entry to the selected output folder."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones that sank it 1,500 miles from the nearest front line."


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
