"""make.fun entry: One Word, One Username, One Reward.

Writes the entrant's own make.fun username — one word and nothing else —
to $MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline.
"""

import os


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    entry = "golden-quasar-38-7753"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
