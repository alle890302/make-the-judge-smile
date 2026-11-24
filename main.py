"""Make the Judge Smile — one line about a small good thing that happened today."""

LINE = (
    "At 7:12 today the baker slipped an extra croissant into my bag, "
    "leaned in, and whispered, 'That one looked lonely.'"
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
