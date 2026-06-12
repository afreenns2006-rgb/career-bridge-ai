import csv

import config


def test_opportunity_csv_has_searchable_columns() -> None:
    with config.OPPORTUNITIES_CSV.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = set(reader.fieldnames or [])

    assert {"title", "category", "skill", "date", "link"}.issubset(columns)


def test_careers_csv_has_recommendation_columns() -> None:
    with config.CAREERS_CSV.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = set(reader.fieldnames or [])

    assert {"career", "career_name"} & columns
    assert "required_skills" in columns
