from pydantic import BaseModel
from typing import List

class Config(BaseModel):
    id: int
    output: bool
    polarity: str
    testpulse: bool
    threshold: float
    csa_res: int
    pzc_res: int
    shp_res: int
    csa_cap: int
    pzc_cap: int
    shp_cap: int

# New model to accept a list of Configs under 'channels'
class ChannelConfigRequest(BaseModel):
    channels: List[Config]