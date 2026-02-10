#!/usr/bin/python3
"""Basic serialization module: save/load Python dictionaries to/from JSON files."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The output JSON file name.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): The input JSON file name.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
