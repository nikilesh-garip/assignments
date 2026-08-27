"""
task02: CSV to JSON Parser (Unassisted implementation)
Parses raw CSV string into a list of dictionaries with type inference.
"""
import csv
import io

def csv_to_json_records(csv_string: str) -> list:
    if not csv_string.strip():
        return []
        
    reader = csv.reader(io.StringIO(csv_string.strip()))
    rows = list(reader)
    if not rows:
        return []
        
    headers = [h.strip() for h in rows[0]]
    records = []
    
    for row in rows[1:]:
        if not row or all(c.strip() == "" for c in row):
            continue
        entry = {}
        for idx, header in enumerate(headers):
            val = row[idx].strip() if idx < len(row) else ""
            # Type conversion
            if val.isdigit():
                val = int(val)
            else:
                try:
                    val = float(val)
                except ValueError:
                    pass
            entry[header] = val
        records.append(entry)
        
    return records
