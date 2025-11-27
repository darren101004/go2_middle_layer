import json
import logging
from typing import Annotated, Literal

import pandas as pd
from fastmcp import FastMCP

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
    req = SportRequest(option=SportOption.DAMP)
    return sport_handler.handle(req)

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

@mcp.tool(description="Sport command: Euler")
async def sport_command_euler(
    roll: float,
    pitch: float,
    yaw: float,
) -> Response:
    params = {
        "roll": roll,
        "pitch": pitch,
        "yaw": yaw,
    }
    req = SportRequest(option=SportOption.EULER, params=params)
    return sport_handler.handle(req)

async def sport_command_move(
    vx: float,
    vy: float,
    vyaw: float,
) -> Response:
    params = {
        "vx": vx,
        "vy": vy,
        "vyaw": vyaw,
    }
    req = SportRequest(option=SportOption.MOVE, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Sit")
async def sport_command_sit() -> Response:
    req = SportRequest(option=SportOption.SIT)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Rise Sit")
async def sport_command_rise_sit() -> Response:
    req = SportRequest(option=SportOption.RISE_SIT)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Speed Level")
async def sport_command_speed_level(
    level: int,
) -> Response:
    params = {
        "level": level,
    }
    req = SportRequest(option=SportOption.SPEED_LEVEL, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Hello")
async def sport_command_hello() -> Response:
    req = SportRequest(option=SportOption.HELLO)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Stretch")
async def sport_command_stretch() -> Response:
    req = SportRequest(option=SportOption.STRETCH)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Content")
async def sport_command_content() -> Response:
    req = SportRequest(option=SportOption.CONTENT)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Dance1")
async def sport_command_dance1() -> Response:
    req = SportRequest(option=SportOption.DANCE1)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Dance2")
async def sport_command_dance2() -> Response:
    req = SportRequest(option=SportOption.DANCE2)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Switch Joystick")
async def sport_command_switch_joystick(
    on: bool,
) -> Response:

    params = {
        "on": on,
    }
    req = SportRequest(option=SportOption.SWITCH_JOYSTICK, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Pose")
async def sport_command_pose(
    flag: bool,
) -> Response:

    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.POSE, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Scrape")
async def sport_command_scrape() -> Response:
    req = SportRequest(option=SportOption.SCRAPE)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Front Flip")
async def sport_command_front_flip() -> Response:
    req = SportRequest(option=SportOption.FRONT_FLIP)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Front Jump")
async def sport_command_front_jump() -> Response:
    req = SportRequest(option=SportOption.FRONT_JUMP)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Front Pounce")
async def sport_command_front_pounce() -> Response:
    req = SportRequest(option=SportOption.FRONT_POUNCE)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Heart")
async def sport_command_heart() -> Response:
    req = SportRequest(option=SportOption.HEART)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Left Flip")
async def sport_command_left_flip() -> Response:
    req = SportRequest(option=SportOption.LEFT_FLIP)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Back Flip")
async def sport_command_back_flip() -> Response:
    req = SportRequest(option=SportOption.BACK_FLIP)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Free Walk")
async def sport_command_free_walk() -> Response:
    req = SportRequest(option=SportOption.FREE_WALK)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Free Bound")
async def sport_command_free_bound(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.FREE_BOUND, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Free Jump")
async def sport_command_free_jump(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.FREE_JUMP, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Free Avoid")
async def sport_command_free_avoid(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.FREE_AVOID, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Walk Upright")
async def sport_command_walk_upright(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.WALK_UPRIGHT, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Cross Step")
async def sport_command_cross_step(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.CROSS_STEP, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Static Walk")
async def sport_command_static_walk() -> Response:
    req = SportRequest(option=SportOption.STATIC_WALK)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Trot Run")
async def sport_command_trot_run() -> Response:
    req = SportRequest(option=SportOption.TROT_RUN)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Hand Stand")
async def sport_command_hand_stand(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.HAND_STAND, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Classic Walk")
async def sport_command_classic_walk(
    flag: bool,
) -> Response:
    params = {
        "flag": flag,
    }
    req = SportRequest(option=SportOption.CLASSIC_WALK, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Auto Recovery Set")
async def sport_command_auto_recovery_set(
    enabled: bool,
) -> Response:
    params = {
        "enabled": enabled,
    }
    req = SportRequest(option=SportOption.AUTO_RECOVERY_SET, params=params)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Auto Recovery Get")
async def sport_command_auto_recovery_get() -> Response:
    req = SportRequest(option=SportOption.AUTO_RECOVERY_GET)
    return sport_handler.handle(req)

@mcp.tool(description="Sport command: Switch Avoid Mode")
async def sport_command_switch_avoid_mode() -> Response:
    req = SportRequest(option=SportOption.SWITCH_AVOID_MODE)
    return sport_handler.handle(req)


if __name__ == "__main__":
    mcp.run()
