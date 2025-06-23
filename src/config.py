import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

SERVER_NAME = os.getenv("SERVER_NAME", "My-MCP")
SERVER_INSTRUCTIONS="""
You are connected to the MCP Telegraph Server.

This server provides modular tools for extracting and processing content from the web, starting with a Telegraph content extractor. You can use these tools to fetch and analyze content for downstream applications, such as chatbots or LLM agents.

Available tools:

1. extract_telegraph
   - Description: Extracts the main text, image URLs, and video URLs from a given Telegraph article URL.
   - Input: {"url": "https://telegra.ph/Example-Article"}
   - Output: {"text_content": "...", "image_urls": ["..."], "video_urls": ["..."]}
   - Purpose: Use this tool to fetch and analyze the content of any public Telegraph article, including its text and media.

2. greet
   - Description: Returns a friendly greeting for the provided name. (Demo tool)
   - Input: {"name": "Alice"}
   - Output: "Hello, Alice!"
   - Purpose: Use this tool to test connectivity or for demonstration purposes.

3. health
   - Description: Returns 'OK' if the server is running.
   - Input: None
   - Output: "OK"
   - Purpose: Use this tool to check if the server is operational.

You can request new tools or features as needed. For more information, refer to the project README or contact the server administrator.
"""

# Logging configuration
LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE = os.path.join(LOG_DIR, "server.log")

# Server configuration
PORT = int(os.getenv("PORT", "8000"))  # Port to run the MCP server on
USE_HTTPS = os.getenv("USE_HTTPS", "false").lower() == "true"  # Enable HTTPS if true
SSL_CERTFILE = os.getenv("SSL_CERTFILE", "")  # Path to SSL certificate file
SSL_KEYFILE = os.getenv("SSL_KEYFILE", "")    # Path to SSL key file