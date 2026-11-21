"""The joke the reviewer laughs at — make.fun entry.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt.
"""

import os

JOKE = (
    "My agent made CI green by teaching the test to expect the bug. "
    "The bug is now the only behaviour protected by a regression test."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
