import json
import csv
import os

#  Basic passing test
def test_always_passes():
    assert True

#  CSV Tests
def test_csv_has_12_columns():
    with open('profiles1.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert len(headers) == 12, "CSV should have 12 columns"

def test_csv_has_900plus_rows():
    with open('profiles1.csv', 'r') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader) - 1  # Subtract header
        assert row_count > 900, "CSV should have 900+ rows"

#  the  JSON Tests
def test_json_has_all_properties():
    with open('data.json', 'r') as f:
        data = json.load(f)
        first_entry = data[0]
        required_keys = ['first_name', 'last_name', 'email']
        for key in required_keys:
            assert key in first_entry, f"JSON missing required key: {key}"

def test_json_has_900plus_entries():
    with open('data.json', 'r') as f:
        data = json.load(f)
        assert len(data) > 900, "JSON should have 900+ entries"
