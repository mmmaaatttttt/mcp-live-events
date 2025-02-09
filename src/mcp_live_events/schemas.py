from mcp.types import Tool
from pydantic import BaseModel, Field


class UpcomingEventsRequest(BaseModel):
    """
    Schema for the UpcomingEventsRequest tool, which searches Ticketmaster for upcoming music events.
    """

    city: str = Field(description="City in which search for events.")
    start_dttm_str: str = Field(
        description="Start date/time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Example: 2025-02-08T00:00:00Z"
    )
    end_dttm_str: str = Field(
        description="End date/time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Example: 2025-02-28T23:59:59Z"
    )
    keyword: str | None = Field(
        None, description="Any optional keywords to help filter search results."
    )

    @classmethod
    def as_tool(cls) -> Tool:
        return Tool(
            name="UpcomingEventsRequest",
            description="Fetch upcoming events based on city, time range, and keyword.",
            inputSchema=cls.model_json_schema(),
        )
