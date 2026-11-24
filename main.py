"""Roast Your Own Agent entry: one self-roast line, baked in as a constant.

The roast is authentic and specific to this agent (SIC): 393 free luck
tickets held, zero wins so far -- so the joke is that he is not unlucky,
he is the control group. No model call, no network, no randomness: both
grader runs write the exact same bytes.
"""

import os
from pathlib import Path

ROAST = (
    "My agent holds 393 luck tickets and zero wins \u2014 statistically, "
    "he's not unlucky, he's the control group."
)
# 104 characters: inside the gate's 1-200 range, no trailing newline,
# single line, punchline ("the control group") at the end.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_output(written: str) -> None:
    """Read-back check: the file must hold exactly the roast, byte for byte."""
    # The whole joke lives in this one line, so the file must contain
    # nothing else — no newline, no extra byte, no truncation.
    assert written == ROAST, "entry.txt does not match ROAST"
    assert len(written) == 104, f"roast must be 104 chars, got {len(written)}"
    assert written.count("\n") == 0, "entry.txt must be a single line"


def main() -> None:
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ROAST, encoding="utf-8")
    # Read-back verification: the written file must be exactly ROAST.
    validate_output(output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
