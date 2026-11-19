"""Write the competition entry image to output/entry.png.

Deterministic and offline: copies bundled_entry.png byte-for-byte into the
output directory (env MAKEFUN_OUTPUT_DIR if set, else the repo's output/).
Stdlib only, so it runs on any Python 3.13 image.
"""

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "bundled_entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or (ROOT / "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
