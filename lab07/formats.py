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
def _parse_scalar(value: str):
    """Приводит строковое значение YAML к числу/булеву/строке."""
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False

    try:                       # целое
        return int(value)
    except ValueError:
        pass
    try:                       # дробное
        return float(value)
    except ValueError:
        pass
    return value


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: 'ключ: значение', списки через '- ', комментарии после #."""
    result: dict = {}
    current_list_key: str | None = None

    for raw in lines:
        # всё после # — комментарий
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        stripped = line.strip()

        # элемент списка
        if stripped == "-" or stripped.startswith("- "):
            if current_list_key is None:
                continue
            item = stripped[1:].strip()
            result[current_list_key].append(_parse_scalar(item))
            continue

        # пара ключ: значение
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                current_list_key = key
                result[key] = []          # открываем список
            else:
                current_list_key = None
                result[key] = _parse_scalar(value)

    return result
def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника по ключу key.

    Поля самой записи важнее: при совпадении ключей берётся значение из row.
    """
    merged: list[dict] = []
    for row in rows:
        k = row.get(key)
        info = extra.get(k, {}) if k is not None else {}
        combined = {**info, **row}   # row перекрывает info
        merged.append(combined)
    return merged
