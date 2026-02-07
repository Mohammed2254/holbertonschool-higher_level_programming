"""HELLO CONVERTING"""
import csv
import json

def convert_csv_to_json(csvfile):
    """ff """
    try:

        with open(csvfile) as file:
            reader = csv.DictReader(file)
            data =[]
            for row in reader:
                data.append(row)
            with open("data.json", "w") as file:
                json.dump(data, file)
        return True


    except:
        return False
