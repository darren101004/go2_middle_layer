import logging
from fastmcp import FastMCP
import asyncio


from src.models.response import Response
from src.models.sport_request import SportRequest
from src.models.sport_option import SportOption
from unitree_sdk2py.go2.sport.sport_client import SportClient
from src.mcps.sport.sport_handler import SportHandler

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

mcp = FastMCP("sport")


sport_client = SportClient()
sport_handler = SportHandler(sport_client)

@mcp.tool(description="Sport command: Damp")
async def sport_command() -> Response:
    stand_down_req = SportRequest(option=SportOption.STAND_DOWN, params={})
    stand_down_response = sport_handler.handle(stand_down_req)
    if not stand_down_response.success:
        await asyncio.sleep(3)
    damp_req = SportRequest(option=SportOption.DAMP, params={})
    return sport_handler.handle(damp_req)

@mcp.tool(description="Sport command: Balance Stand")
async def sport_command_balance_stand() -> Response:
    req = SportRequest(option=SportOption.BALANCE_STAND)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Stop Move")
async def sport_command_stop_move() -> Response:
    req = SportRequest(option=SportOption.STOP_MOVE)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Stand Up")
async def sport_command_stand_up() -> Response:
    req = SportRequest(option=SportOption.STAND_UP)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Stand Down")
async def sport_command_stand_down() -> Response:
    req = SportRequest(option=SportOption.STAND_DOWN)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Recovery Stand")
async def sport_command_recovery_stand() -> Response:
    req = SportRequest(option=SportOption.RECOVERY_STAND)
    return sport_handler.handle(req)

async def sport_command_move(
    vx: float,
    vy: float,
    vyaw: float,
) -> Response:
    
    
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    
    # Unit: m/s
    # Default mode: vx [-1.5, 1.5], vy [-0.6, 0.6], vyaw [-1.0, 1.0]
    # Stair climbing: vx [-0.7, 0.7], vy [-0.5, 0.5], vyaw [-1.0, 1.0]
    # Climbing height: vx [-0.5, 0.5], vy [-0.4, 0.4], vyaw [-0.6, 0.6]

    def limit(val, min_val, max_val):
        return max(min_val, min(max_val, val))

    vx_limited = limit(vx, -1.5, 1.5)
    vy_limited = limit(vy, -0.6, 0.6)
    vyaw_limited = limit(vyaw, -1.0, 1.0)
    
    params = {
        "vx": vx_limited,
        "vy": vy_limited,
        "vyaw": vyaw_limited,
    }
    move_req = SportRequest(option=SportOption.MOVE, params=params)
    return sport_handler.handle(move_req)


@mcp.tool(description="Sport command: Speed Level")
async def sport_command_speed_level(
    level: int,
) -> Response:
    params = {
        "level": level,
    }
    req = SportRequest(option=SportOption.SPEED_LEVEL, params=params)
    return sport_handler.handle(req)


if __name__ == "__main__":
    mcp.run()
