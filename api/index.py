"""
Vercel Python serverless entrypoint for Google Workspace MCP server.
"""
import os
import sys

_root = os.path.dirname(os.path.abspath(__file__))
_root_project = os.path.dirname(_root)
sys.path.insert(0, _root_project)

from fastmcp_server import mcp

app = mcp.http_app(path="/mcp")

def handler(event, context):
    """Vercel Python serverless handler."""
    return app(event, context)