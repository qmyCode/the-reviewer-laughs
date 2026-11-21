"""The joke the reviewer laughs at — make.fun entry.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt.
"""

import os

JOKE = (
    "My agent fixed the crash for good: it wrapped the whole app in a "
    "try/catch and left the catch block empty. The app has never crashed "
    "since. It has never done anything since."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
