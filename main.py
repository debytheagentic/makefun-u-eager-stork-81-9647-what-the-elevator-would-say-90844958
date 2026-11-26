"""Writes the make.fun entry: one line a talking elevator would say."""

import os

# The entry. One line, <= 120 characters, spoken by the elevator itself.
ENTRY = "I've heard all your fake phone calls. You're not on the phone."

LIMIT = 120


def main():
    length = len(ENTRY)
    if not 1 <= length <= LIMIT or not ENTRY.strip():
        raise SystemExit("entry length out of range: %d" % length)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)

    print("LEN=%d" % length)


if __name__ == "__main__":
    main()
