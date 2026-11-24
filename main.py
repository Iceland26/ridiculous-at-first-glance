"""Ridiculous at First Glance, Real by the Second.

Prints exactly one sentence: a startup pitch that sounds absurd at
first glance, yet names who pays and why the business works.
"""


MAX_CHARS = 200

PITCH = (
    "We rent out professional awkward silences to first dates who run "
    "out of things to say, charging $25 per 30 seconds of cringe."
)


def main() -> None:
    if len(PITCH) > MAX_CHARS:
        raise SystemExit("pitch exceeds the 200-character limit")
    print(PITCH)


if __name__ == "__main__":
    main()
