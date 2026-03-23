"""Tests for displaying product data from JSON, CSV, or SQLite in Flask."""

import sqlite3
import unittest
from unittest.mock import patch

from task_04_db import DB_FILE, app


class TestTask04Db(unittest.TestCase):
    """Verify product display behavior across file and database sources."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_products_route_reads_json_source(self):
        response = self.client.get("/products?source=json")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", content)
        self.assertIn("Coffee Mug", content)

    def test_products_route_reads_csv_source(self):
        response = self.client.get("/products?source=csv")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Notebook", content)
        self.assertIn("Office Supplies", content)

    def test_products_route_reads_sql_source(self):
        response = self.client.get("/products?source=sql")
        content = response.get_data(as_text=True)

        self.assertTrue(DB_FILE.exists())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", content)
        self.assertIn("Coffee Mug", content)
        self.assertNotIn("Notebook", content)

    def test_products_route_filters_by_id(self):
        response = self.client.get("/products?source=sql&id=2")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Coffee Mug", content)
        self.assertNotIn("Laptop", content)

    def test_products_route_rejects_invalid_source(self):
        response = self.client.get("/products?source=xml")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Wrong source", content)

    def test_products_route_handles_unknown_id(self):
        response = self.client.get("/products?source=csv&id=99")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Product not found", content)

    def test_products_route_handles_database_errors(self):
        with patch("task_04_db.sqlite3.connect", side_effect=sqlite3.Error):
            response = self.client.get("/products?source=sql")

        content = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Database error", content)


if __name__ == "__main__":
    unittest.main()
