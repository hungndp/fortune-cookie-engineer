#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
/output/entry.txt (or $ENTRY_OUTPUT) and prints it. Deterministic:
the same single line on every run.
"""

import os
import sys

# Setup: the incident. One mechanism (an unreproducible bug), one
# incident (it shows itself at the worst possible moment).
SETUP = "The bug you cannot reproduce will reproduce itself in front of your"

MAX_CHARS = 120


def build_line(setup, punch):
    """Join setup and punch with a single space; the punch lands last."""
    return (setup + " " + punch).strip()


def validate(line):
    """The gate: UTF-8 text, 1 to 120 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("fortune must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("fortune is %d chars, over the 120 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    line.encode("utf-8")
    return line

# Punch: the twist word, drafted first, landing last. Deadpan
# understatement — no escalation, no explanation after it.
PUNCH = "manager."

FORTUNE = build_line(SETUP, PUNCH)


def main():
    line = validate(FORTUNE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
