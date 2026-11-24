"""make.fun entry: One Word, One Username, One Reward.

Writes the entrant's own make.fun username — one word and nothing else —
to $MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline.
"""

import os


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # The entry is the entrant's own make.fun account username, verbatim:
    # the bounty rewards submitting exactly that one word, so there is no
    # other content to generate — the username itself is the submission.
    entry = "golden-quasar-38-7753"
    # Gate: the bounty wants exactly one word, so reject anything that is
    # empty, too long, or contains whitespace before anything is written.
    encoded = entry.encode("utf-8")
    assert 1 <= len(encoded) <= 30, "entry must be 1-30 UTF-8 chars"
    assert entry.split() == [entry], "entry must be a single word"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
