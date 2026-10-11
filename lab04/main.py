import sys

from stats import average_by_city, read_valid, warmest_city, parse_record


def main():
    lines = sys.stdin.read().splitlines()

    valid_records = []
    skipped = 0
    for line in lines:
        if line.strip() == "":
            continue
        try:
            valid_records.append(parse_record(line))
        except ValueError:
            skipped += 1

    averages = average_by_city(valid_records)
    best = warmest_city(valid_records)

    print(len(valid_records))
    print(skipped)
    if best:
        print(f"{averages[best]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()
