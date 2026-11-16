#!/usr/bin/env python3
"""ai-excited-01: copy the entry image to /output/entry.png.

Deterministic: the output is a byte-for-byte copy of the image the
repository holds, so two runs always produce identical bytes.
Standard library only; no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
