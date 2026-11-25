#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader (round 2).

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated, to /output/entry.txt. Deterministic: the same bytes
on every run.
"""

import os

FORTUNE = (
    "Congratulations! Your fortune is the same as your portfolio: "
    "liquidated. Please enjoy this cookie instead."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the competition gate before writing: one line, at most
    # 20 words of plain text, 1 to 160 characters. Fail loudly rather
    # than silently shipping an entry the gate would refuse.
    words = FORTUNE.split()
    if not 1 <= len(FORTUNE) <= 160:
        raise SystemExit(f"gate: fortune is {len(FORTUNE)} chars, must be 1-160")
    if len(words) > 20:
        raise SystemExit(f"gate: fortune is {len(words)} words, must be at most 20")
    if "\n" in FORTUNE:
        raise SystemExit("gate: fortune must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
