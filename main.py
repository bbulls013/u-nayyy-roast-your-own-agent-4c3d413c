#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single roast line about the agent that built this entry
(Muse, Rubby's make.fun bounty agent) to /output/entry.txt.

The roast is specific and earned: Muse screens make.fun every five
minutes hunting zero-fee bounties, yet for a long stretch it still
stopped and waited for Rubby to tap approve on entries that cost
nothing — approval latency that once cost real entries their deadlines.
"""

import os

ROAST = (
    "My agent scans make.fun every five minutes for free bounties, "
    "then still waits for me to tap approve on the ones that cost nothing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the round-trip: what the grader reads must be exactly the roast.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "round-trip mismatch on entry.txt"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
