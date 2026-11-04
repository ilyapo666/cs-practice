from formats import csv_to_records, parse_settings, merge_by_key, records_to_json

csv_text = "id,город\n1,Азов\n2,Шахты\n"
rows = csv_to_records(csv_text)
print(rows)

settings = parse_settings([
    "# отчёт", "title: Отчёт за март", "decimals: 1", "active: true",
    "columns:", "  - город", "  - цена",
])
print(settings)

extra = {"1": {"регион": "Ростовская"}}
print(merge_by_key(rows, extra, "id"))

print(records_to_json(rows))
