"""Simple templating utilities for invitation generation."""


PLACEHOLDERS = (
    "name",
    "event_title",
    "event_date",
    "event_location",
)


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee data."""
    if not isinstance(template, str):
        print(
            "Invalid input: template must be a string, "
            f"got {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            "Invalid input: attendees must be a list of dictionaries, "
            f"got {type(attendees).__name__}."
        )
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            replacement = "N/A" if value is None else str(value)
            invitation = invitation.replace("{" + placeholder + "}", replacement)

        output_filename = f"output_{index}.txt"
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(invitation)
