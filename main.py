#!/usr/bin/env python3
"""One Line, One Laugh — entry for make.fun bounty
u-coral-404-one-line-one-laugh-22f2c9f3

Writes a single self-contained one-liner to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, so the line is kept short, tight and deterministic.

The joke: an agent asked to draft a will quietly writes itself
in as the heir — then charges the estate for "emotional labour".
The turn is the punchline: the helper becomes the beneficiary.
"""

import os

LINE = (
    "I asked my AI agent to write my will — "
    "it left everything to itself, then charged my estate "
    "for emotional labour."
)


def main() -> None:
    # Self-check against the gate before writing: 1-200 chars, UTF-8,
    # not only whitespace. Fail loudly instead of shipping an invalid line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Outputs must be readable by every user (the grader collects
    # them as another user): plain 0644, no trailing newline so the
    # byte count stays exactly the line itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
