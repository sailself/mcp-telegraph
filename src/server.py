import os
from fastmcp import FastMCP
from src.tools.telegraph_extractor import extract_telegraph_content
from src.config import (
    SERVER_NAME,
    SERVER_INSTRUCTIONS
)

mcp = FastMCP(name=SERVER_NAME, instructions=SERVER_INSTRUCTIONS)



@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def health() -> str:
    return "OK"

@mcp.tool
def extract_telegraph(url: str) -> dict:
    try:
        return extract_telegraph_content(url)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()