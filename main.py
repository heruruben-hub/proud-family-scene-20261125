#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Feel Proud: A Family Scene".

Writes one short family scene (one or two lines, 1-280 characters) to
/output/entry.txt, exactly as the gate requires: UTF-8 text, not only
whitespace, no trailing newline.
"""

import os

ENTRY_TEXT = (
    "Dad finally fixed the wobbly table leg after three years, and Mum "
    "clapped like he had won the World Cup. The kids chanted his name, "
    "the dog barked along, and Dad stood there grinning, holding the "
    "screwdriver like a trophy."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
