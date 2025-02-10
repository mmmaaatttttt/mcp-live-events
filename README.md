# MCP Live Events Server

`mcp-live-events` is a Model Context Protocol (MCP) server that integrates with
the Ticketmaster API to provide real-time event data. It allows AI agents to
fetch concert and event details dynamically.

## Features

- 🎟️ Integrates with the Ticketmaster API to search for events
- 🗣️ Formats API responses for ease of LLM interpretation

## Setup

### Prerequisites

Ensure you have the following installed:

- [uv](https://github.com/astral-sh/uv) (used for package management)
- Python 3.13+
- A [Ticketmaster](https://developer.ticketmaster.com/explore/) API key (free to
  use, but rate limited)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/mmmaaatttttt/mcp-live-events.git
    cd mcp-live-events
    ```

2. Install dependencies:

    ```sh
    uv venv
    uv sync
    ```

3. Set up your environment variables, i.e. the Ticketmaster API key. This can
   either be placed in a `.env` file in this repository, following the pattern
   of the `.env.example` file, or it can be placed in an "env" section of this
   server's configuration in your MCP client.

   Note that on the Ticketmaster developer portal, the API key is named
   "Consumer Key."

### Running the server

```sh
uv run mcp-live-events
```

If it's successful, you should see `MCP Live Event server is running!` print to
your terminal.

## Resources

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)
- [MCP Server Demo Quickstart](https://modelcontextprotocol.io/quickstart/server)
