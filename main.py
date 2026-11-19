"""Write the news-image-20261119 entry to output/entry.png.

Offline, stdlib-only and deterministic: copies bundled_entry.png
byte-for-byte into $MAKEFUN_OUTPUT_DIR (default: the repo's output/).
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    gen = ROOT / "gen" / "make_entry.py"
    result = subprocess.run(
        [sys.executable, str(gen)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "gen/make_entry.py failed")
    print("wrote output/entry.png 1024x1024")


if __name__ == "__main__":
    main()
