#!/usr/bin/env python3
"""Write the world-news summary for 11 November 2026 to the output directory.

The summary is stored beside this program and copied out unchanged, so both
runs produce the same bytes. OUT_DIR overrides the default /output.
"""
import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    text = (here / "summary.txt").read_text(encoding="utf-8")
    out_dir = Path(os.environ.get("OUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
