def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for path in paths:
        filename = path.rsplit("/", 1)[-1]
        ext = filename.rsplit(".", 1)[1].lower() if "." in filename else ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count("/") for p in paths)
    return min(p for p in paths if p.count("/") == max_depth)


def human_size(n_bytes: int) -> str:
    units = ("Б", "КБ", "МБ", "ГБ", "ТБ")
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    value = float(n_bytes)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f"{value:.1f} {units[idx]}"
