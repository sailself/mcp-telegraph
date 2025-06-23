# MCP Telegraph Server

A modular MCP server for LLM-powered applications, starting with a Telegraph content extractor. Designed for easy integration with bots (e.g., Telegram) and LLMs (e.g., Gemini).

## Features

- **Telegraph Content Extraction:** Extracts text, images, and videos from any Telegraph page.
- **Modular Tooling:** Easily add more tools for your LLM app.
- **Ready for Integration:** Use as a backend for bots or LLM agents.

## Installation

```bash
# Clone the repository
https://github.com/yourusername/mcp-telegraph.git
cd mcp-telegraph

# Create and activate a virtual environment
python -m venv venv
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

This project uses environment variables for configuration. Copy `.env.example` to `.env` and fill in your secrets:

```bash
cp .env.example .env
```

Edit `.env` and set your values, for example:
```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
```

Environment variables are loaded automatically at server startup.

## Usage

Start the server:
```bash
python src/server.py
```

## API

### `extract_telegraph`
Extracts content from a Telegraph URL.

**Request:**
```json
{
  "url": "https://telegra.ph/your-article"
}
```

**Response:**
```json
{
  "text_content": "...",
  "image_urls": ["..."],
  "video_urls": ["..."]
}
```
If an error occurs:
```json
{
  "error": "Error message here."
}
```

### `greet`
Demo tool.

**Request:**
```json
{
  "name": "Alice"
}
```

**Response:**
```json
"Hello, Alice!"
```

### `health`
Health check endpoint.

**Request:**
No parameters.

**Response:**
```json
"OK"
```

## Adding More Tools

Add new tools in `src/tools/` and register them in `src/server.py` using the `@mcp.tool` decorator. Example:

```python
from src.tools.my_new_tool import my_new_function

@mcp.tool
def my_tool(args):
    return my_new_function(args)
```

## For Telegram Bots & LLMs

- Call the server's endpoints from your bot or LLM agent.
- Example: Use the `extract_telegraph` tool to fetch and summarize Telegraph articles.

## License

MIT
