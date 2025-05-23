import csv
import json

def convert_csv_to_json(csv_filename, json_filename):
    """
    Converts profiles1.csv to data.json
    """
    data = []
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    convert_csv_to_json('profiles1.csv', 'data.json')