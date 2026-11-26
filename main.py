"""One-Liner Laughs entry.

Writes a single original joke line to /output/entry.txt.
The joke is one line, 1-200 characters, with a clear setup and a
surprise payoff.
"""

import os

JOKE = "I organized my entire life into folders, but happiness is still in Downloads, buried under 400 files named final_final_v2.pdf."


def main():
    # The gate requires 1-200 characters, UTF-8, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
