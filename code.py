import csv
import json
import sys

def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=4)

if __name__ == "__main__":
    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    csv_to_json(csv_file, json_file)
