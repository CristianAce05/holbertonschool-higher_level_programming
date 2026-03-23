"""Tests for displaying product data from JSON or CSV in Flask."""

import unittest

from task_03_files import app


class TestTask03Files(unittest.TestCase):
    """Verify product display behavior for valid and invalid inputs."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_products_route_reads_json_source(self):
        response = self.client.get("/products?source=json")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", content)
        self.assertIn("Coffee Mug", content)
        self.assertIn("799.99", content)

    def test_products_route_reads_csv_source(self):
        response = self.client.get("/products?source=csv")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Notebook", content)
        self.assertIn("Office Supplies", content)
        self.assertIn("6.50", content)

    def test_products_route_filters_by_id(self):
        response = self.client.get("/products?source=json&id=2")
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


if __name__ == "__main__":
    unittest.main()
