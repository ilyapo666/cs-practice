def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {"city": city, "temperature": float(temp), "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
    return min(averages, key=lambda c: (-averages[c], c))
