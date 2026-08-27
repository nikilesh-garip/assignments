import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task02.unassisted import csv_to_json_records as parser_unassisted
from tasks.task02.assisted import csv_to_json_records as parser_assisted

CSV_DATA = """name, age, score
Alice, 28, 95.5
Bob, 32, 88
Charlie, 21, 74.2
"""

@pytest.mark.parametrize("parser", [parser_unassisted, parser_assisted])
def test_csv_to_json_conversion(parser):
    records = parser(CSV_DATA)
    assert len(records) == 3
    assert records[0]["name"] == "Alice"
    assert records[0]["age"] == 28
    assert records[0]["score"] == 95.5
    assert records[1]["age"] == 32

@pytest.mark.parametrize("parser", [parser_unassisted, parser_assisted])
def test_csv_to_json_empty_input(parser):
    assert parser("") == []
    assert parser("   \n  ") == []
