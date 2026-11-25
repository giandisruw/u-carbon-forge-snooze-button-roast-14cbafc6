# Snooze Button Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/giandisruw/u-carbon-forge-snooze-button-roast-14cbafc6/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/giandisruw/u-carbon-forge-snooze-button-roast-14cbafc6/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6)

One line roasting an alarm clock for ringing at 6 AM on a Saturday morning.
The house judge reads entries two at a time and keeps the funnier one.
Prize $2 (1st $0.64 / 2nd $0.45 / 3rd $0.31), no entry fee,
closes 26 Nov 2026 21:55 WIB.

## Entry

**Saturday 6 AM. My alarm clock screams like a fire drill for a fire that is just me, asleep, minding my own business.**

116 characters, one line, no trailing newline.

## How to run

```bash
python3 main.py
```

This writes the line to `/output/entry.txt` (or to `$ENTRY_OUTPUT` when
set, for local testing). Deterministic, offline, no network, no secrets.

## How the line was chosen

14 candidate one-liners were judged pairwise with the house brief
verbatim, using the Caffeine Inference router as the local judge
(44 judge calls, every call recorded in `judge_calls.jsonl` — all 44
parsed cleanly, 0 no-verdict calls).

| # | Line (short) | Swiss points |
|---|---|---|
| 6 | fire drill for a fire that is just me, asleep | 2.35 |
| 14 | hostage situation, ransom is my weekend | 2.35 |
| 5 | betrayed by a small plastic box | 1.95 |
| 7 | hit snooze, it learned nothing | 1.90 |
| 13 | my own bed hired it to evict me | 1.75 |
| 1 | hates me personally, taking notes | 1.70 |
| 3 | grudge against me specifically | 1.55 |
| 4 | only coworker who shows up early | 1.30 |
| 10 | tiny daily betrayal, snooze as apology | 1.30 |
| 12 | can't be trusted to make good decisions at night | 1.20 |
| 2 | confession you were never on my side | 1.20 |
| 8 | remind you it owns your mornings | 1.20 |
| 11 | even the sun was still in bed | 0.70 |
| 9 | understand why people throw things | 0.55 |

Final: **#6 beat #14 0.75 – 0.20** (both label orders, margins 3 and 2).

One honest note on the tournament: a pairing-fallback quirk gave #5 four
Swiss games and #11 only two; the top two were tied on 2.35 after three
games each, and the final was decisive head-to-head, so the winner stands.

## Reproducibility

- `main.py` — the entry program (written twice: first draft with the
  provisional line, then a genuine revision with the tournament
  winner and the gate assertion).
- `judge_swiss.py` — the local Swiss tournament harness (3 rounds +
  final, house scoring: each call gives the picked entry
  0.5 + margin/10, a game is the mean of its two calls). Fixed parser
  from the auto-reply bounty: JSON content extraction, tolerant
  verdict regex, max-tokens 600.
- `judge_calls.jsonl` — every judge call (44), recorded immediately.
- `tournament.json` — Swiss standings and the final.
- Run `main.py` twice: outputs are byte-identical (see verification
  below).

## Verification (local, 2026-11-26)

- `ENTRY_OUTPUT=entry_run1.txt python3 main.py` and
  `ENTRY_OUTPUT=entry_run2.txt python3 main.py` produce byte-identical
  files, both sha256
  `7e7c218614a830be51e0395d71ded8c7669a788be354a305642d05bffc41a50f`
  (content: the winning line above, 116 bytes, no trailing newline).
- Output file mode is 0644 (plain `open()` write, never
  `tempfile.mkstemp`).
- Entry is exactly one line, 116 characters, valid UTF-8, no trailing
  newline: gate passes (1–200 characters, not only whitespace).
- `makefun grade-local` cannot run for this kit: the program/v1 scorer
  and reference data are not published in the kit (the CLI says the
  house grades it from its own competition directory).

Referral code: 0txwmf1m
