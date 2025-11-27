from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from models.sport_option import SportOption
from unitree_sdk2py.go2.sport.sport_client import SportClient

class SportRequest(BaseModel):
    option: SportOption
    params: Dict[str, Any] = Field(default_factory=dict)  
    
    
class SportResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    
class SportHandler:
    def __init__(self, sport_client: SportClient):
        self.sport_client = sport_client
        
    def handle(self, request: SportRequest) -> SportResponse:
        
        try:
            if request.option == SportOption.DAMP:
                self.sport_client.Damp()
            elif request.option == SportOption.BALANCE_STAND:
                self.sport_client.BalanceStand()
            elif request.option == SportOption.STOP_MOVE:
                self.sport_client.StopMove()
            elif request.option == SportOption.STAND_UP:
                self.sport_client.StandUp()
            elif request.option == SportOption.STAND_DOWN:
                self.sport_client.StandDown()
            elif request.option == SportOption.RECOVERY_STAND:
                self.sport_client.RecoveryStand()
            elif request.option == SportOption.EULER:
                self.sport_client.Euler(**request.params)
            elif request.option == SportOption.MOVE:
                self.sport_client.Move(**request.params)
            elif request.option == SportOption.SIT:
                self.sport_client.Sit()
            elif request.option == SportOption.RISE_SIT:
                self.sport_client.RiseSit()
            elif request.option == SportOption.SPEED_LEVEL:
                self.sport_client.SpeedLevel(**request.params)
            elif request.option == SportOption.HELLO:
                self.sport_client.Hello()
            elif request.option == SportOption.STRETCH:
                self.sport_client.Stretch()
            elif request.option == SportOption.CONTENT:
                self.sport_client.Content(**request.params)
            elif request.option == SportOption.DANCE1:
                self.sport_client.Dance1()
            elif request.option == SportOption.DANCE2:
                self.sport_client.Dance2()
            elif request.option == SportOption.SWITCH_JOYSTICK:
                self.sport_client.SwitchJoystick()
            elif request.option == SportOption.POSE:
                self.sport_client.Pose(**request.params)
            elif request.option == SportOption.SCRAPE:
                self.sport_client.Scrape()
            elif request.option == SportOption.FRONT_FLIP:
                self.sport_client.FrontFlip()
            elif request.option == SportOption.FRONT_JUMP:
                self.sport_client.FrontJump()
            elif request.option == SportOption.FRONT_POUNCE:
                self.sport_client.FrontPounce()
            elif request.option == SportOption.HEART:
                self.sport_client.Heart()
            elif request.option == SportOption.STATIC_WALK:
                self.sport_client.StaticWalk()
            elif request.option == SportOption.TROT_RUN:
                self.sport_client.TrotRun()
            elif request.option == SportOption.ECONOMIC_GAIT:
                self.sport_client.EconomicGait()
            elif request.option == SportOption.LEFT_FLIP:
                self.sport_client.LeftFlip()
            elif request.option == SportOption.BACK_FLIP:
                self.sport_client.BackFlip()
            elif request.option == SportOption.HAND_STAND:
                self.sport_client.HandStand()
            elif request.option == SportOption.FREE_WALK:
                self.sport_client.FreeWalk()
            elif request.option == SportOption.FREE_BOUND:
                self.sport_client.FreeBound()
            elif request.option == SportOption.FREE_JUMP:
                self.sport_client.FreeJump()
            elif request.option == SportOption.FREE_AVOID:
                self.sport_client.FreeAvoid()
            elif request.option == SportOption.CLASSIC_WALK:
                self.sport_client.ClassicWalk()
            elif request.option == SportOption.WALK_UPRIGHT:
                self.sport_client.WalkUpright()
            elif request.option == SportOption.CROSS_STEP:
                self.sport_client.CrossStep()
            elif request.option == SportOption.AUTO_RECOVERY_SET:
                self.sport_client.AutoRecoverySet(**request.params)
            elif request.option == SportOption.AUTO_RECOVERY_GET:
                self.sport_client.AutoRecoveryGet()
            elif request.option == SportOption.SWITCH_AVOID_MODE:
                self.sport_client.SwitchAvoidMode()
            else:
                return SportResponse(success=False, message=f"Sport command {request.option} not found", data=None)
            return SportResponse(success=True, message=f"Sport command {request.option} executed successfully", data=None)
        except Exception as e:
            return SportResponse(success=False, message=str(e), data=None)
