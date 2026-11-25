#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry (u-carbon-forge-snooze-button-roast-14cbafc6).

Writes one line roasting an alarm clock for ringing at 6 AM on a Saturday
morning to /output/entry.txt (or $ENTRY_OUTPUT for local testing).

Deterministic, offline, no network, no secrets.

The line: tournament winner out of 14 candidates, 3 Swiss rounds + final,
judged pairwise with the house brief verbatim by the Caffeine Inference
router (44 judge calls, every call recorded in judge_calls.jsonl).
Swiss: #6 and #14 tied at 2.35 points; final: #6 beat #14 0.75 - 0.25.
"""
import os

LINE = (
    "Saturday 6 AM. My alarm clock screams like a fire drill for a fire "
    "that is just me, asleep, minding my own business."
)


def main():
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
