from contextlib import AsyncExitStack
import logging
import os
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from starlette.middleware import Middleware
from starlette.middleware.exceptions import ExceptionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from ddtrace.trace import tracer
from ddtrace import patch
from ddtrace.contrib.asgi import TraceMiddleware
from fastapi import FastAPI, Request
from mcps.sport.main import mcp as sport_mcp
from unitree_sdk2py.core.channel import ChannelFactoryInitialize


logger = logging.getLogger(__name__)

ChannelFactoryInitialize(0, "wlan0")


middleware = [ Middleware(ExceptionMiddleware)]
sport_mcp_http = sport_mcp.http_app(
    path="/mcp",
    middleware=middleware,
    stateless_http=True,
)


@asynccontextmanager
async def combined_lifespan(app: FastAPI):
    try:
        logger.info(
            "Initialize all singleton services at application startup."
        )

        async with AsyncExitStack() as stack:
            for mcp in [
                sport_mcp_http,
            ]:
                logger.info(f"Entering lifespan for {mcp.__module__}")
                await stack.enter_async_context(mcp.lifespan(app))

            yield
    finally:
        pass


app = FastAPI(name="go2-middle-layer", lifespan=combined_lifespan)

app.mount(
    "/sport",
    sport_mcp_http,
    name="sport-legacy",
)


@app.get("/health")
def health():
    return {"message": "OK"}


if __name__ == "__main__":
    import argparse
    import uvicorn

    port = int(os.environ.get("PORT", 8000))  # read from env or default 8000

    parser = argparse.ArgumentParser(description="Run MCP Server")
    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=port,
        help="Port to run the server on (default: 8000)",
    )

    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="debug")
