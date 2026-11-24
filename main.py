"""One-Liner Marathon entry: a single deadpan joke about an umbrella.

Writes exactly one line of text to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR when running locally). Deterministic,
standard library only, no network, no secrets.
"""

import os
from pathlib import Path

JOKE = (
    "My umbrella flipped inside out in the rain, so I just walked home "
    "holding it like a flag of surrender."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError(
            f"entry must be 1-280 non-whitespace characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
