import asyncio
import logging
import time

from fastmcp import FastMCP
from mcps.sport.sport_handler import SportHandler
from models.response import Response
from models.sport_option import SportOption
from models.sport_request import SportRequest


logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

mcp = FastMCP("sport")

sport_handler = SportHandler()

PI = 3.1415926

@mcp.tool(description="Sport command: Stop Move")
async def stop_move() -> Response:
    req = SportRequest(option=SportOption.STOP_MOVE)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Stand Up")
async def stand_up() -> Response:
    
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    stand_up_req = SportRequest(option=SportOption.STAND_UP, params={})
    res = sport_handler.handle(stand_up_req)
    return res

@mcp.tool(description="Sport command: Stand Down")
async def stand_down() -> Response:
    stand_up_req = SportRequest(option=SportOption.STAND_UP, params={})
    _ = sport_handler.handle(stand_up_req)
    

    stand_down_req = SportRequest(option=SportOption.STAND_DOWN, params={})
    res = sport_handler.handle(stand_down_req)
    return res

@mcp.tool(description="Sport command: Go Ahead 0.3 meters")
async def go_ahead() -> Response:
    vx = 0.3
    vy = 0
    vyaw = 0
    distance = 1 # 1 meter but it is 0.3 meters in the real world
    time_to_move = distance / vx
    
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    
    # Unit: m/s
    # Default mode: vx [-1.5, 1.5], vy [-0.6, 0.6], vyaw [-1.0, 1.0]
    # Stair climbing: vx [-0.7, 0.7], vy [-0.5, 0.5], vyaw [-1.0, 1.0]
    # Climbing height: vx [-0.5, 0.5], vy [-0.4, 0.4], vyaw [-0.6, 0.6]
    params = {
        "vx": vx,
        "vy": vy,
        "vyaw": vyaw,
    }
    
    start_time = time.time()
    res = None
    while time.time() - start_time < time_to_move:
        move_req = SportRequest(option=SportOption.MOVE, params=params)
        res = sport_handler.handle(move_req)
        if not res.success:
            return res
        await asyncio.sleep(0.5)
        
    stop_move_req = SportRequest(option=SportOption.STOP_MOVE, params={})
    _ = sport_handler.handle(stop_move_req)
    return res


@mcp.tool(description="Sport command: Go Back 0.3 meters")
async def go_back() -> Response:
    vx = -0.3
    vy = 0
    vyaw = 0
    distance = 1 # 1 meter but it is 0.3 meters in the real world
    time_to_move = abs(distance / vx)
    
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    params = {
        "vx": vx,
        "vy": vy,
        "vyaw": vyaw,
    }
    
    start_time = time.time()
    res = None
    while time.time() - start_time < time_to_move:
        move_req = SportRequest(option=SportOption.MOVE, params=params)
        res = sport_handler.handle(move_req)
        if not res.success:
            return res
        await asyncio.sleep(0.5)
    
    stop_move_req = SportRequest(option=SportOption.STOP_MOVE, params={})
    _ = sport_handler.handle(stop_move_req)
    return res


@mcp.tool(description="Sport command: Turn left 90 degrees")
async def turn_left() -> Response:
    
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    
    vyaw = 0.5
    alpha = 60 # 60 degrees but it is 90 degrees in the real world
    time_to_turn = (PI * alpha / 180) / vyaw

    start_time = time.time()
    res = None
    params = {
        "vx": 0,
        "vy": 0,
        "vyaw": vyaw,
    }
    while time.time() - start_time < time_to_turn:
        turn_req = SportRequest(option=SportOption.MOVE, params=params)
        res = sport_handler.handle(turn_req)
        if not res.success:
            return res
        await asyncio.sleep(0.5)
    
    return res


@mcp.tool(description="Sport command: Turn right 90 degrees")
async def turn_right() -> Response:
    recovery_stand_req = SportRequest(option=SportOption.RECOVERY_STAND, params={})
    _ = sport_handler.handle(recovery_stand_req)
    
    balance_stand_req = SportRequest(option=SportOption.BALANCE_STAND, params={})
    _ = sport_handler.handle(balance_stand_req)
    
    vyaw = -0.5
    alpha = 60 # 60 degrees but it is 90 degrees in the real world
    time_to_turn = abs((PI * alpha / 180) / vyaw)

    start_time = time.time()
    res = None
    params = {
        "vx": 0,
        "vy": 0,
        "vyaw": vyaw,
    }
    while time.time() - start_time < time_to_turn:
        turn_req = SportRequest(option=SportOption.MOVE, params=params)
        res = sport_handler.handle(turn_req)
        if not res.success:
            return res
        await asyncio.sleep(0.5)
    
    stop_move_req = SportRequest(option=SportOption.STOP_MOVE, params={})
    _ = sport_handler.handle(stop_move_req)
    return res

if __name__ == "__main__":
    mcp.run()