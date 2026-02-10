#!/usr/bin/python3
"""Create a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """Load and return a Python object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
