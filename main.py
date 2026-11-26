import os

ENTRY = "My calendar is so full it now books meetings to discuss why I'm in so many meetings."
MAX_CHARS = 199  # the gate accepts 1..199 characters


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
