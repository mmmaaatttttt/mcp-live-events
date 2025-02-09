from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .schemas import UpcomingEventsRequest
from .utils import format_events

load_dotenv()

server = Server("live-events-finder")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools."""
    tools = [
        UpcomingEventsRequest.as_tool(),
    ]
    return tools


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[TextContent]:
    """Handle tool execution requests."""
    from .events_api_client import EventsApiClient

    assert name == "UpcomingEventsRequest", f"Unknown tool: {name}"

    data = await EventsApiClient().fetch_events(**arguments)

    return [TextContent(type="text", text=format_events(data))]


async def main():
    """Start the MCP server."""
    try:
        options = server.create_initialization_options()
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream, options)
    except Exception as e:
        raise
