"""Tests for the basic Flask Jinja application."""

import unittest

from task_01_jinja import app


class TestTask01Jinja(unittest.TestCase):
    """Verify routes render the expected templates and shared layout."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_route_renders_index_template(self):
        response = self.client.get("/")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to My Flask App", content)
        self.assertIn("<li>Flask</li>", content)
        self.assertIn('href="/about"', content)
        self.assertIn("&copy; 2024 My Flask App", content)

    def test_about_route_renders_about_template(self):
        response = self.client.get("/about")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("About Us", content)
        self.assertIn("This page shares a little more information", content)
        self.assertIn('href="/contact"', content)

    def test_contact_route_renders_contact_template(self):
        response = self.client.get("/contact")
        content = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Contact Us", content)
        self.assertIn("find contact information", content)
        self.assertIn('href="/"', content)


if __name__ == "__main__":
    unittest.main()
