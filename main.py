#!/usr/bin/env python3
"""Entry for make.fun news-image-20261120.

Copies the bundled front-page image (entry.png, drawn for Friday
20 November 2026) to the output directory. Standard library only:
no network, no randomness, no clock, so two runs write identical
bytes.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("wrote %s" % target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
