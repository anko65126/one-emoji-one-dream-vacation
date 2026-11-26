"""Entry program for the 'One Emoji, One Dream Vacation' make.fun bounty.

The entry is a single emoji: a palm tree. One small green palm
against the sky says the whole dream at once — warm sand, slow
afternoons, nowhere to be, no inbox in sight. It needs no words at
all, which is exactly the point of the bounty. The program writes
exactly that one emoji to /output/entry.txt (an optional first
argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

WORD = "\U0001F334"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(WORD) <= 8, "entry must be one emoji (1-8 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD + "\n", encoding="utf-8")
    print(f"wrote {target} ({WORD!r}, {len(WORD)} chars)")


if __name__ == "__main__":
    main(sys.argv)
