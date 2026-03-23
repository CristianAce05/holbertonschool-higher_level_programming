"""Example entry point for the invitation generator."""

from pathlib import Path

from task_00_intro import generate_invitations


def main():
    """Load the template file and generate sample invitations."""
    template_path = Path(__file__).with_name("template.txt")
    template_content = template_path.read_text(encoding="utf-8")

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
        {
            "name": "Charlie",
            "event_title": "AI Summit",
            "event_date": None,
            "event_location": "Boston",
        },
    ]

    generate_invitations(template_content, attendees)


if __name__ == "__main__":
    main()
