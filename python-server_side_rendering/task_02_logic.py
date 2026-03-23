"""Flask application that renders dynamic content from a JSON file."""

import json
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("items.json")


def load_items():
    """Load the items list from the JSON data file."""
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("items", [])


@app.route("/items")
def items():
    """Render the items page with data from the JSON file."""
    return render_template("items.html", items=load_items())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
