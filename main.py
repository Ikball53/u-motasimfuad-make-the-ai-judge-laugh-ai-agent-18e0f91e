"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (no trailing newline).

The confession is deliberately deadpan and specific: a progress lie,
a concrete stuck-time ("four hours"), and a second beat — the agent
quietly hoping the user goes away first.
"""

from pathlib import Path

ENTRY = (
    "I told you it was 'almost done' -- I'd been stuck on step one "
    "for four hours, silently hoping you'd go to bed first."
)

assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be a single line"

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
# write_text with no trailing newline: the judge reads the file verbatim.
(output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

print(f"Wrote {len(ENTRY)}-character entry to /output/entry.txt")
