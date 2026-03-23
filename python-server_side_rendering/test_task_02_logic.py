"""Tests for the dynamic Flask template exercise."""

import json
import unittest

from task_02_logic import DATA_FILE, app


class TestTask02Logic(unittest.TestCase):
    """Verify the items route renders JSON-backed content correctly."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        self.original_data = DATA_FILE.read_text(encoding="utf-8")

    def tearDown(self):
        DATA_FILE.write_text(self.original_data, encoding="utf-8")

    def test_items_route_renders_all_items(self):
        response = self.client.get("/items")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Items List", content)
        self.assertIn("<li>Python Book</li>", content)
        self.assertIn("<li>Flask Mug</li>", content)
        self.assertIn("<li>Jinja Sticker</li>", content)

    def test_items_route_shows_empty_message(self):
        DATA_FILE.write_text(json.dumps({"items": []}), encoding="utf-8")

        response = self.client.get("/items")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("No items found", content)
        self.assertNotIn("<li>", content)


if __name__ == "__main__":
    unittest.main()
