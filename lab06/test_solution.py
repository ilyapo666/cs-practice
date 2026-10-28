from solution import count_by_extension, deepest_path, human_size


def main() -> None:
    paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

    assert count_by_extension(paths) == {
        "pdf": 1, "txt": 1, "png": 1, "": 1,
    }, count_by_extension(paths)

    assert deepest_path(paths) == "docs/img/logo.png", deepest_path(paths)
    assert deepest_path([]) == ""

    assert human_size(0) == "0 Б"
    assert human_size(900) == "900 Б"
    assert human_size(1023) == "1023 Б"
    assert human_size(1024) == "1.0 КБ"
    assert human_size(1536) == "1.5 КБ"
    assert human_size(5 * 1024 * 1024) == "5.0 МБ"

    print("All checks passed ✔")


if __name__ == "__main__":
    main()
