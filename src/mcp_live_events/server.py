from mcp.server.fastmcp import FastMCP

from .utils import format_events
from .events_api_client import EventsApiClient

mcp = FastMCP("mcp-live-events")

@mcp.tool()
async def get_upcoming_events(city: str, start_dttm_str: str, end_dttm_str: str, keyword: str | None = None) -> str:
    """
    Get upcoming music events for a city.
    
    Args:
        city: City in which to search for events.
        start_dttm_str: Start date/time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Example: 2025-02-08T00:00:00Z
        end_dttm_str: Start date/time in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Example: 2025-02-10T00:00:00Z
        keyword: Any optional keywords to help filter search results.
    """

    data = await EventsApiClient().fetch_events(city=city, start_dttm_str=start_dttm_str, end_dttm_str=end_dttm_str, keyword=keyword)

    return format_events(data)
