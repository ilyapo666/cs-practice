"""Перевод между форматами хранения данных: CSV, YAML (учебный), JSON."""

import json


def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком -> список словарей. Значения остаются строками."""
    lines = text.splitlines()
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    records: list[dict] = []

    for raw in lines[1:]:
        if not raw.strip():
            continue
        values = [v.strip() for v in raw.split(",")]
        # выравниваем длину до заголовка
        if len(values) < len(headers):
            values += [""] * (len(headers) - len(values))
        records.append(dict(zip(headers, values)))

    return records
