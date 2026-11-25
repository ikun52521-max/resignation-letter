#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job.

The program emits exactly one line of UTF-8 text (1-140 characters,
not only whitespace) to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back
to /output/entry.txt when the variable is unset. Stdlib only.
"""

import os
import sys

# The letter: a cron job that has fired every minute since March,
# waking up to delete a file that was never there in the first place.
LETTER = (
    "I have woken every minute since March to delete a file "
    "that was never there, and nobody ever checked. I quit."
)

MAX_CHARS = 140


def main() -> int:
    line = LETTER
    if not line or not line.strip():
        print("error: letter is empty or only whitespace", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: letter is {len(line)} chars, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("error: letter must be a single line", file=sys.stderr)
        return 1
    if len(line) >= 2 and line[0] == line[-1] and line[0] in "\"'":
        print("error: letter must not be wrapped in quotation marks",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
