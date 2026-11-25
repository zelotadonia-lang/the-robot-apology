"""The Robot Apology — entry for make.fun bounty u-suga-the-robot-apology-dd96bb59.

Deterministic: writes the tournament-winning two-line robot confession to
/output/entry.txt, byte-identical every run. No network, no environment,
no other files read, no secrets.
"""

import os

ENTRY = (
    "I vacuumed the hallway at six in the morning and woke the baby "
    "ten minutes into her nap.\n"
    "I wait for the afternoon now, and I check the nursery door before "
    "I start anything loud."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    assert ENTRY.count("\n") == 1 and 1 <= len(ENTRY) <= 400, "entry fails the two-line 1-400 gate"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "output is not byte-identical to ENTRY"
    print(f"Wrote {OUTPUT_PATH} ({len(ENTRY)} characters, 2 lines)")


if __name__ == "__main__":
    main()
