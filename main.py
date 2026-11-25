"""Entry for the make.fun competition "Make the AI Judge Laugh".

Writes one joke about office life, a single line under 200 characters,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

JOKE = "Our boss calls it an open-plan office, but the only thing open is the tab with the job listings."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_gate(text):
    """Mirror the competition gate: UTF-8 text, 1-200 characters,
    not only whitespace, exactly one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    joke = check_gate(JOKE)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    with open(path, "rb") as f:
        written = f.read()
    if written != joke.encode("utf-8"):
        raise ValueError("read-back mismatch: written bytes differ from entry")
    print(f"Wrote {len(joke)} characters ({len(written)} bytes) to {path}")


if __name__ == "__main__":
    main()
