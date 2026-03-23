"""Flask application that displays product data from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"
DB_FILE = BASE_DIR / "products.db"


def normalize_product(product):
    """Convert raw product data into a consistent display format."""
    return {
        "id": int(product["id"]),
        "name": product["name"],
        "category": product["category"],
        "price": float(product["price"]),
    }


def create_database():
    """Create and populate the SQLite database when it does not exist yet."""
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
            """
        )
        cursor.executemany(
            """
            INSERT OR REPLACE INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
            """,
            [
                (1, "Laptop", "Electronics", 799.99),
                (2, "Coffee Mug", "Home Goods", 15.99),
            ],
        )
        connection.commit()


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


def read_products_from_db():
    """Read product data from the SQLite database."""
    with sqlite3.connect(DB_FILE) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products ORDER BY id")
        rows = cursor.fetchall()

    return [normalize_product(dict(row)) for row in rows]


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

    try:
        if source == "json":
            product_list = read_products_from_json()
        elif source == "csv":
            product_list = read_products_from_csv()
        elif source == "sql":
            product_list = read_products_from_db()
        else:
            return render_template("product_display.html", error="Wrong source")
    except sqlite3.Error:
        return render_template("product_display.html", error="Database error")

    filtered_products = filter_products(product_list, product_id)
    if product_id is not None and not filtered_products:
        return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=filtered_products)


create_database()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
