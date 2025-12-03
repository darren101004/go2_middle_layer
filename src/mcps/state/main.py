import logging
from fastmcp import FastMCP

from src.models.response import Response
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_
from unitree_sdk2py.core.channel import ChannelSubscriber

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

TOPIC_STATE = "rt/sportmodestate"
sub = ChannelSubscriber(TOPIC_STATE, SportModeState_)
sub.Init()

mcp = FastMCP("state")

@mcp.tool(description="Get State")
async def get_state() -> Response:
    try:
        msg: SportModeState_ = sub.Read()
        if msg is not None:
            data = {
                "stamp": msg.stamp,
                "error_code": msg.error_code,
                "imu_state": msg.imu_state,
                "mode": msg.mode,
                "progress": msg.progress,
                "gait_type": msg.gait_type,
                "foot_raise_height": msg.foot_raise_height,
                "position": msg.position,
                "body_height": msg.body_height,
                "velocity": msg.velocity,
                "yaw_speed": msg.yaw_speed,
                "range_obstacle": msg.range_obstacle,
                "foot_force": msg.foot_force,
                "foot_position_body": msg.foot_position_body,
                "foot_speed_body": msg.foot_speed_body,
                "path_point": msg.path_point,
            }
            return Response(success=True, message="State retrieved successfully", data=data, code=200)
    except Exception as e:
        return Response(success=False, message=f"Error retrieving state: {e}", data=None, code=500)