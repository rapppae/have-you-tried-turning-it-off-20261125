"""Entry for make.fun bounty "Have You Tried Turning It Off?".

Entry text (146 characters, limit: at most 199 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "Let us start by turning it off and on again — while it restarts, I will quietly Google your error message and pretend I knew the answer all along."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
