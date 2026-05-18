#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.ERROR)

attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    {
        "name": "Bob",
        "event_title": "Data Science Workshop",
        "event_date": "2023-08-20",
        "event_location": "San Francisco"
    },
    {
        "name": "Charlie",
        "event_title": "AI Summit",
        "event_date": None,
        "event_location": "Boston"
    }
]


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendees data."""

    # Validate template type
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    # Validate attendees type
    if (
        not isinstance(attendees, list)
        or not all(isinstance(item, dict) for item in attendees)
    ):
        logging.error("Attendees must be a list of dictionaries.")
        return

    # Check empty template
    if not template:
        logging.error(
            "Template is empty, no output files generated."
        )
        return

    # Check empty attendees list
    if not attendees:
        logging.error(
            "No data provided, no output files generated."
        )
        return
    for i, attendee in enumerate(attendees, start=1):
        new_template = template
        new_template = new_template.replace("{name}", attendee.get("name", "") or "N/A")
        new_template = new_template.replace("{event_title}", attendee.get("event_title", "") or "N/A")
        new_template = new_template.replace("{event_date}", attendee.get("event_date", "") or "N/A")
        new_template = new_template.replace("{event_location}", attendee.get("event_location", "") or "N/A")
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as file:
                file.write(new_template)
        except OSError as e:
            logging.error(f"Error writing file {filename}: {e}")

