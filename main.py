"""Entry for make.fun bounty "Two Lines to Your Past Self".

Writes two lines of text -- a warning to the writer's past self about
one specific moment, and one sentence on why that moment mattered --
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when the variable is
unset, matching the grader container).

The text is a constant, so the program is deterministic: every run
writes exactly the same bytes. Before writing, the program checks the
text against the bounty gate (UTF-8 text of 1 to 280 characters, not
only white space, exactly two lines) and fails loudly if it ever
drifts out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "Do not say 'ship it' just because the deploy went green on the first try at 6 p.m. on a Friday.\n"
    "That one easy win is why you stopped reading the logs, and the next failure waited in them for weeks, written out in plain sight, before you ever looked."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("error: the entry is empty", file=sys.stderr)
        return 1
    if "\r" in text:
        print("error: the entry must use plain newline line endings", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        print("error: the entry must be exactly two non-empty lines", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the entry is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(text, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != text:
        print("error: written text differs from the entry", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
