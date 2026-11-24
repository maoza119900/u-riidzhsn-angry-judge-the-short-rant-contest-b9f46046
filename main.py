"""Short funny rant about the office printer for u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "I fixed the office printer, and to celebrate it printed a test page, then another test page, then a diagnostic report about the test pages, and now the toner I bought to fix it is gone."

# Entry is 185 characters, inside the 400-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
