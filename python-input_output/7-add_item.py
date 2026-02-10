#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a JSON file."""

import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
items = []

# Load existing items if the file exists
if Path(file_name).exists():
    items = load_from_json_file(file_name)

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save updated list to the JSON file
save_to_json_file(items, file_name)
