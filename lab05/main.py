from pathlib import Path

from logstats import count_levels, format_report, top_errors

TOP_N = 10


def main() -> None:
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, TOP_N)

    report = format_report(counts, errors)
    out_path = Path(__file__).with_name("report.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as out:
        out.write(report)


if __name__ == "__main__":
    main()
