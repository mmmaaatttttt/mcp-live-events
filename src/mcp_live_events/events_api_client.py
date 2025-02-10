from dotenv import load_dotenv
import os

import httpx

load_dotenv()


class EventsApiClient:
    def __init__(self):
        self.base_url = "https://app.ticketmaster.com/discovery/v2"
        self.api_key = os.environ.get("TICKETMASTER_API_KEY")
        if not self.api_key:
            raise ValueError("Ticketmaster API key missing!")

    async def fetch_events(
        self,
        city: str,
        start_dttm_str: str,
        end_dttm_str: str,
        classification_name: str = "Music",
        keyword: str | None = None,
    ) -> dict | None:
        async with httpx.AsyncClient() as client:
            try:
                params = {
                    "apikey": self.api_key,
                    "city": city,
                    "startDateTime": start_dttm_str,
                    "endDateTime": end_dttm_str,
                    "classificationName": classification_name,
                    "size": 100,
                }
                if keyword:
                    params["keyword"] = keyword
                response = await client.get(
                    f"{self.base_url}/events.json",
                    params=params,
                    timeout=30.0,
                )
                response.raise_for_status()
                return response.json()
            except Exception:
                return None
