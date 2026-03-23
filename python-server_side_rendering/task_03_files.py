"""Flask application that displays product data from JSON or CSV files."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"


def read_products_from_json():
    """Read product data from the JSON file."""
    with JSON_FILE.open("r", encoding="utf-8") as file:
        products = json.load(file)

    return [normalize_product(product) for product in products]


def read_products_from_csv():
    """Read product data from the CSV file."""
    with CSV_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [normalize_product(row) for row in reader]


def normalize_product(product):
    """Convert raw product data into a consistent display format."""
    return {
        "id": int(product["id"]),
        "name": product["name"],
        "category": product["category"],
        "price": float(product["price"]),
    }


def filter_products(products, product_id):
    """Filter the products list by id when an id is provided."""
    if product_id is None:
        return products

    try:
        target_id = int(product_id)
    except ValueError:
        return []

    return [product for product in products if product["id"] == target_id]


@app.route("/products")
def products():
    """Render products from the requested source and optional id filter."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        product_list = read_products_from_json()
    elif source == "csv":
        product_list = read_products_from_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    filtered_products = filter_products(product_list, product_id)
    if product_id is not None and not filtered_products:
        return render_template(
            "product_display.html",
            error="Product not found",
        )

    return render_template("product_display.html", products=filtered_products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
