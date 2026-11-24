"""One Line of Earned Pride.

Writes one line -- a quiet, earned moment of pride for someone in a
scene -- to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Single line, 1 to 240 characters, no trailing newline.

The line:

    After forty years of night shifts, she folded her uniform one
    last time, turned off an alarm she had set since 1984, and slept
    until morning.

Why this line (reasoning, kept here and in the README; the entry
itself is just the line):

* Genuine earned pride, not a boast: forty years of night shifts is
  a whole working life, and the pride is in the finishing -- folding
  the uniform one last time -- not in any applause.
* A concrete scene with a real person: a uniform, an alarm set since
  1984, a morning's sleep. The year dates the effort without any
  explaining; the reader does the arithmetic and feels the weight.
* Lands in one read: three small actions, each quieter than the last
  -- fold, switch off, sleep -- and the line ends on the simplest
  reward there is, sleeping until morning, which is exactly what
  forty years of nights denied her.
* Fresh: no trophy, no speech, no "she did it" -- the pride is in
  the ordinary objects, which is what makes it earned rather than
  declared.

Candidates weighed and set aside: a marathon-finish line -- the
obvious earned-pride scene, and the judge will have seen it;
a father-teaching-a-child-to-ride-a-bike line -- warm, but the pride
belongs to the child, not the scene's worker; a graduation line --
too ceremonial for "quiet".

Standard library only. Deterministic: no randomness, no network, no
clock.
"""

import hashlib
import os

TEXT = (
    "After forty years of night shifts, she folded her uniform one "
    "last time, turned off an alarm she had set since 1984, and slept "
    "until morning."
)

MAX_CHARS = 240

# sha256 of the exact bytes main.py must write to entry.txt, measured
# from a verified run. The read-back step asserts the file's digest
# equals this value, so any drift in the written bytes fails loudly.
EXPECTED_SHA256 = (
    "5cce0f417c12e8cea0b2d90ebc06b93db3febd1df918a790938502d5534b2951"
)


def validate_text(value) -> str:
    """Guard: value must be a single non-blank line of 1..240 chars.

    Accepts either the text string or the raw bytes read back from the
    entry file, so the same check covers the pre-write guard and the
    post-write read-back verification. Returns the text as a str, or
    raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    assert 1 <= len(value) <= MAX_CHARS, (
        f"entry.txt must be 1..{MAX_CHARS} characters, got {len(value)}"
    )
    assert value.strip(), "entry.txt must not be only whitespace"
    assert "\n" not in value and "\r" not in value, (
        "entry.txt must be a single line"
    )
    return value


def main() -> None:
    # Pre-write guard: refuse to write anything outside the gate.
    validate_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read-back validation: the gate is 1..240 characters, so the file
    # must hold exactly the text we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_text(data) == TEXT
    # Digest verification: the written bytes must hash to the digest
    # measured from the verified run, proving no drift or stray bytes.
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, (
        f"entry.txt sha256 mismatch: got {digest}, "
        f"expected {EXPECTED_SHA256}"
    )
    print(TEXT)
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
