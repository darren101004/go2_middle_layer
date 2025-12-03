import logging
from fastmcp import FastMCP

from src.models.response import Response
from unitree_sdk2py.go2.video.video_client import VideoClient


logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

mcp = FastMCP("camera")
video_client = VideoClient()
video_client.SetTimeout(3.0)
video_client.Init()

@mcp.tool(description="Camera command: Capture Image")
async def camera_command_capture_image() -> Response:
    code, data = video_client.GetImageSample()
    image_data = None
    import base64
    if code == 0 and data is not None:
        image_data = base64.b64encode(bytes(data)).decode('utf-8')
    else:
        return Response(success=False, message=f"Failed to capture image. Code: {code}", data=None, code=400)
    return Response(success=True, message=f"Image captured successfully. Code: {code}", data=image_data, code=200)

if __name__ == "__main__":
    mcp.run()
