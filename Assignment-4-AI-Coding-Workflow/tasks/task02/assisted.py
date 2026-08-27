"""
task02: CSV to JSON Parser (AI-Assisted implementation)
Parses raw CSV string into a list of dictionaries with type inference.
"""
import csv
import io

def parse_val(v: str):
    v_clean = v.strip()
    if v_clean.isdigit():
        return int(v_clean)
    try:
        return float(v_clean)
    except ValueError:
        return v_clean

def csv_to_json_records(csv_string: str) -> list:
    cleaned = csv_string.strip()
    if not cleaned:
        return []
    
    reader = csv.DictReader(io.StringIO(cleaned))
    records = []
    for row in reader:
        records.append({k.strip(): parse_val(v) for k, v in row.items() if k is not None})
    return records
