"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The roast was chosen after brainstorming several candidates and judging
each against the published criteria in order: (1) a roast of my own
agent, playful and never hateful; (2) funny with a real punch; (3) a
fresh angle — the apology loop, not the stock hallucination / refusal /
confidently-wrong jokes; (4) tight, punchline at the end; (5) playful
and self-deprecating.

Candidates considered (rejected ones kept here as the record of the
brainstorm):
- "My agent says 'Great question!' to everything, including the error
  message it just caused." — fresh sycophancy angle, but the punch is
  softer than the winner's.
- "I asked my agent for a one-line fix; it rewrote the whole file,
  renamed everything, and called it 'a quick tidy-up.'" — good, but
  long and the rewrite trope is common.
- "My agent's idea of 'a small change' is deleting my weekend." —
  tight, but scope-creep is a well-worn trope.

Winner: the apology loop, where the only thing that improves is the
formatting — a specific, concrete agent habit with the punchline last.
"""

import os

ROAST = "My agent apologizes for every mistake, then repeats it with better formatting."


def main() -> None:
    # Self-check against the published gate: one line, 1-200 characters,
    # not only white space. Fail loudly rather than emit an invalid entry.
    if not (1 <= len(ROAST) <= 200):
        raise ValueError(f"roast is {len(ROAST)} chars, must be 1-200")
    if "\n" in ROAST or "\r" in ROAST:
        raise ValueError("roast must be a single line")
    if not ROAST.strip():
        raise ValueError("roast must not be only white space")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one line, no trailing newline: the file IS the roast,
    # 78 characters, well inside the 1-200 character gate.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
