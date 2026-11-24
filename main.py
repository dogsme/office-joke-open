"""Office Joke Open entry: write one office joke line to /output/entry.txt."""

import os

JOKE = "Our 15-minute standup kept running over, so management scheduled a weekly meeting to discuss shortening it \u2014 it's now in its third week."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
