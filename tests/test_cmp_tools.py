import ast
import asyncio
import httpx
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
import io
import pandas as pd
import uuid
task_id = str(uuid.uuid4())
BASE_URL = f"http://localhost:8001/financial_datasets/mcp"

from fastmcp import Client
from fastmcp.client import StreamableHttpTransport



async def test_list_tools(client: Client[StreamableHttpTransport] = None):
    """Test listing the MCP tools"""
    async with client:
        assert client.is_connected()
        tools = await client.list_tools()
        print(f"Total tools: {len(tools)}")
        for tool in tools:
            print(tool.name)

async def test_stand_up():
    streamable_http_client = Client(
        transport=StreamableHttpTransport(
            url=BASE_URL
        )
    )
    async with streamable_http_client:
        assert streamable_http_client.is_connected()
        arguments = {}
        stand_up = await streamable_http_client.call_tool(name="stand_up", arguments=arguments)
        print(stand_up)
        
async def test_all_cmp_tools():
    await test_list_tools()
    await test_stand_up()

if __name__ == "__main__":
    asyncio.run(test_all_cmp_tools())