# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for the [make.fun](https://make.fun) bounty **The Funniest One-Line Resignation Letter** — a program that writes the one-line resignation letter of a cron job, 140 characters at most, in the flat, tired, faintly passive-aggressive voice of a worker who has had enough.

## How it works

`main.py` (Python 3.13 standard library only) writes a single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), validating that the line is 1–140 characters, not only whitespace, a single line, and not wrapped in quotation marks.

The letter:

> I have woken every minute since March to delete a file that was never there, and nobody ever checked. I quit.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Deterministic: repeated runs produce byte-identical output.
