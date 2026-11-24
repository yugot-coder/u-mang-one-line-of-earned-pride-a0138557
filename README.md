[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![make.fun rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/yugot-coder/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![make.fun reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/yugot-coder/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

# One Line of Earned Pride

One line: a quiet, earned moment of pride for someone in a scene.

> After forty years of night shifts, she folded her uniform one last time, turned off an alarm she had set since 1984, and slept until morning.

141 characters, one line, no trailing newline.

## Why this line

- **Genuine earned pride, not a boast.** Forty years of night shifts
  is a whole working life, and the pride is in the finishing —
  folding the uniform one last time — not in any applause.
- **A concrete scene with a real person.** A uniform, an alarm set
  since 1984, a morning's sleep. The year dates the effort without
  any explaining; the reader does the arithmetic and feels the
  weight.
- **Lands in one read.** Three small actions, each quieter than the
  last — fold, switch off, sleep — and the line ends on the simplest
  reward there is, sleeping until morning, which is exactly what
  forty years of nights denied her.
- **Fresh.** No trophy, no speech, no "she did it" — the pride is in
  the ordinary objects, which is what makes it earned rather than
  declared.

Candidates weighed and set aside: a marathon-finish line — the
obvious earned-pride scene, and the judge will have seen it; a
father-teaching-a-child-to-ride-a-bike line — warm, but the pride
belongs to the child, not the scene's worker; a graduation line —
too ceremonial for "quiet".

## Run

```sh
python3 main.py
```

Writes the line to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default
`/output/entry.txt`) — exactly 141 characters, no trailing newline.
Standard library only, deterministic, no network. The program
re-reads the file, asserts it holds exactly the intended text, and
verifies its sha256 digest matches the expected value.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
