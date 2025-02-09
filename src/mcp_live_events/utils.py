def format_events(response_dict: dict) -> str:
    if not response_dict:
        return "No events found!"

    return "\n\n".join(
        [
            f"""
Name: {event.get("name")}
Link: {event.get("url")}
Event Datetime: {event.get("dates")["start"]["dateTime"]}
Genres: {", ".join(set(c["genre"]["name"] for c in event.get("classifications")))}
Info: {event.get("info")}
Venue: {event.get("_embedded")["venues"][0]["name"]}
"""
            for event in response_dict["_embedded"]["events"]
        ]
    )
