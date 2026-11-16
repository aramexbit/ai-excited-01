#!/usr/bin/env python3
"""ai-excited-01: copy the entry image to /output/entry.png.

Deterministic: the output is a byte-for-byte copy of the image the
repository holds, so two runs always produce identical bytes.
The copy is verified before the program exits: the output must match
the source in size and SHA-256, or the program fails loudly instead
of shipping a corrupt image.
Standard library only; no network.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if os.path.getsize(SRC) != os.path.getsize(OUT):
        raise SystemExit("entry.png: size mismatch after copy")
    if sha256_file(SRC) != sha256_file(OUT):
        raise SystemExit("entry.png: SHA-256 mismatch after copy")


if __name__ == "__main__":
    main()
