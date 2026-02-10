#!/usr/bin/python3
"""Convert CSV data to JSON format using serialization."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON and save as data.json.

    Args:
        csv_filename (str): The input CSV file name.

    Returns:
        bool: True if conversion succeeds, False if an error occurs.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
