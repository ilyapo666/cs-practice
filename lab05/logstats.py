
from collections import Counter

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    text = line.rstrip("\r\n")
    if not text.strip():
        raise ValueError("пустая строка")

    parts = text.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("строка не содержит трёх частей")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"неизвестный уровень: {level!r}")
    if not time:
        raise ValueError("пустое время")
    if not message.strip():
        raise ValueError("пустое сообщение")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts: Counter = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] += 1
        else:
            counts[event["level"]] += 1
    return dict(counts)


def top_errors(lines, n: int) -> list[list]:
    if n <= 0:
        return []
    counter: Counter = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            counter[event["message"]] += 1

    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in ordered[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for message, count in errors:
        lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"
