#!/usr/bin/env python3
"""One-Liner Laugh Lab — the robot vacuum's excuse after eating a sock.

Entry program: writes the one-line excuse to /output/entry.txt.
Deterministic, no network, same bytes on every run.
"""

import os

# The line, as named segments joined at runtime: the excuse states the
# vacuum's minimising plea, the punch gives its tasting notes.
_SETUP = "Just a taste, I swear."
_PUNCH = "The notes: cotton, regret, and a hint of foot."

LINE = " ".join((_SETUP, _PUNCH))

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    # Segments must join cleanly: exactly one space, no stray
    # whitespace, each segment a single sentence.
    assert text == _SETUP + " " + _PUNCH, "segments did not join cleanly"
    assert _SETUP.endswith(".") and _PUNCH.endswith("."), (
        "each segment must end with a period"
    )
    assert text == text.strip(), "entry has leading/trailing whitespace"
    # Pre-write self-check: the gate wants UTF-8 text of 1-200
    # characters, not only whitespace, on a single line.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert encoded.decode("utf-8") == text, "entry is not clean UTF-8"
    assert "\n" not in text, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Post-write re-read self-check: the bytes on disk are exactly
    # the chosen line, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "entry.txt does not match the chosen line"
    assert 1 <= len(on_disk) <= 200, "entry.txt length outside 1-200"


if __name__ == "__main__":
    main()
