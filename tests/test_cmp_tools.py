import asyncio
from fastmcp import Client
from fastmcp.client import StreamableHttpTransport

BASE_URL = "http://localhost:8000/sport/mcp"

async def test_list_tools():
    client = Client(
        transport=StreamableHttpTransport(url=BASE_URL)
    )
    async with client:
        assert client.is_connected()
        tools = await client.list_tools()
        print(f"Total tools: {len(tools)}")
        for tool in tools:
            print(tool.name)

async def test_stand_up():
    client = Client(
        transport=StreamableHttpTransport(url=BASE_URL)
    )
    async with client:
        assert client.is_connected()
        result = await client.call_tool("stand_up", {})
        print(result)

async def test_stand_down():
    client = Client(
        transport=StreamableHttpTransport(url=BASE_URL)
    )
    async with client:
        assert client.is_connected()
        result = await client.call_tool("stand_down", {})
        print(result)

async def test_all_cmp_tools():
    await test_list_tools()
    await test_stand_up()
    await test_stand_down()

if __name__ == "__main__":
    asyncio.run(test_all_cmp_tools())