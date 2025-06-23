import os
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from fastmcp import FastMCP
from tools.telegraph_extractor import extract_telegraph_content
from config import (
    SERVER_NAME,
    SERVER_INSTRUCTIONS,
    LOG_DIR,
    LOG_FILE,
    PORT,
)

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure Python logging
logger = logging.getLogger("mcp_server")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", backupCount=7, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Optional: also log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

mcp = FastMCP(name=SERVER_NAME, instructions=SERVER_INSTRUCTIONS, port=PORT)

# Example log on server start
logger.info(f"Starting {SERVER_NAME}")
logger.debug(f"Server instructions: {SERVER_INSTRUCTIONS}")

@mcp.tool
def greet(name: str) -> str:
    logger.info(f"greet tool called with name={name}")
    return f"Hello, {name}!"

@mcp.tool
def health() -> str:
    logger.info("health check called")
    return "OK"

@mcp.tool
def extract_telegraph(url: str) -> dict:
    logger.info(f"extract_telegraph tool called with url={url}")
    try:
        result = extract_telegraph_content(url)
        logger.debug(f"extract_telegraph result: {result}")
        return result
    except Exception as e:
        logger.error(f"extract_telegraph error: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()