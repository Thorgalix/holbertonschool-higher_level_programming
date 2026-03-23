#!/usr/bin/python3
"""Simple templating utility for invitation generation."""


def generate_invitations(template, attendees):
	"""Generate output_X.txt invitation files from a template and attendee data.

	Args:
		template (str): Invitation template containing placeholders.
		attendees (list[dict]): List of attendee dictionaries.
	"""
	if not isinstance(template, str):
		print(
			"Invalid input: template must be a string, got "
			f"{type(template).__name__}."
		)
		return

	if not isinstance(attendees, list):
		print(
			"Invalid input: attendees must be a list of dictionaries, got "
			f"{type(attendees).__name__}."
		)
		return

	if not all(isinstance(attendee, dict) for attendee in attendees):
		print("Invalid input: attendees must be a list of dictionaries.")
		return

	if template == "":
		print("Template is empty, no output files generated.")
		return

	if len(attendees) == 0:
		print("No data provided, no output files generated.")
		return

	placeholders = ["name", "event_title", "event_date", "event_location"]

	for index, attendee in enumerate(attendees, start=1):
		output = template
		for key in placeholders:
			value = attendee.get(key)
			if value is None:
				value = "N/A"
			output = output.replace("{" + key + "}", str(value))

		filename = f"output_{index}.txt"
		try:
			with open(filename, "w", encoding="utf-8") as file:
				file.write(output)
		except OSError as error:
			print(f"Error writing {filename}: {error}")
