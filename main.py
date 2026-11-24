"""Office joke entry for make.fun: Make the AI Judge Laugh — the Office Joke Open.

Writes one single-line joke about office life (at most 200 characters)
to /output/entry.txt, deterministically.
"""

import os

LINE = ("I hit reply-all to say 'please stop replying all' and 47 people replied all to agree.")

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
