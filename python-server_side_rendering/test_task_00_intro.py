"""Unit tests for the invitation generator."""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout

from task_00_intro import generate_invitations


class TestGenerateInvitations(unittest.TestCase):
    """Test cases for generate_invitations."""

    def setUp(self):
        self.template = (
            "Hello {name},\n\n"
            "You are invited to the {event_title} on {event_date} "
            "at {event_location}.\n"
        )

    def test_creates_sequential_output_files(self):
        attendees = [
            {
                "name": "Alice",
                "event_title": "Python Conference",
                "event_date": "2023-07-15",
                "event_location": "New York",
            },
            {
                "name": "Bob",
                "event_title": "Data Science Workshop",
                "event_date": "2023-08-20",
                "event_location": "San Francisco",
            },
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            current_dir = os.getcwd()
            os.chdir(temp_dir)
            try:
                generate_invitations(self.template, attendees)

                self.assertTrue(os.path.exists("output_1.txt"))
                self.assertTrue(os.path.exists("output_2.txt"))

                with open("output_1.txt", "r", encoding="utf-8") as file:
                    content = file.read()

                self.assertIn("Hello Alice,", content)
                self.assertIn("Python Conference", content)
            finally:
                os.chdir(current_dir)

    def test_missing_values_are_replaced_with_na(self):
        attendees = [
            {
                "name": "Charlie",
                "event_title": "AI Summit",
                "event_date": None,
                "event_location": "Boston",
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            current_dir = os.getcwd()
            os.chdir(temp_dir)
            try:
                generate_invitations(self.template, attendees)

                with open("output_1.txt", "r", encoding="utf-8") as file:
                    content = file.read()

                self.assertIn("on N/A at Boston", content)
            finally:
                os.chdir(current_dir)

    def test_empty_template_logs_message_and_creates_no_files(self):
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as temp_dir:
            current_dir = os.getcwd()
            os.chdir(temp_dir)
            try:
                with redirect_stdout(output):
                    generate_invitations("", [{"name": "Alice"}])

                self.assertEqual(
                    output.getvalue().strip(),
                    "Template is empty, no output files generated.",
                )
                self.assertEqual(os.listdir(temp_dir), [])
            finally:
                os.chdir(current_dir)

    def test_empty_attendees_logs_message_and_creates_no_files(self):
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as temp_dir:
            current_dir = os.getcwd()
            os.chdir(temp_dir)
            try:
                with redirect_stdout(output):
                    generate_invitations(self.template, [])

                self.assertEqual(
                    output.getvalue().strip(),
                    "No data provided, no output files generated.",
                )
                self.assertEqual(os.listdir(temp_dir), [])
            finally:
                os.chdir(current_dir)

    def test_invalid_template_type_logs_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            generate_invitations(None, [])

        self.assertEqual(
            output.getvalue().strip(),
            "Invalid input: template must be a string, got NoneType.",
        )

    def test_invalid_attendees_type_logs_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            generate_invitations(self.template, "not-a-list")

        self.assertEqual(
            output.getvalue().strip(),
            "Invalid input: attendees must be a list of dictionaries, got str.",
        )

    def test_non_dictionary_attendee_logs_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            generate_invitations(self.template, [{"name": "Alice"}, "Bob"])

        self.assertEqual(
            output.getvalue().strip(),
            "Invalid input: attendees must be a list of dictionaries.",
        )


if __name__ == "__main__":
    unittest.main()
