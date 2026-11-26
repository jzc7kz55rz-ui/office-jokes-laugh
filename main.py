import os

ENTRY = "My calendar is so full it now books meetings to discuss why I'm in so many meetings."
MAX_CHARS = 199


def entry_text():
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS
    return text


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
