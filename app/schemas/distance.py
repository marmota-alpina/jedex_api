from typing import Any

from pydantic import BaseModel


class DistanceBase(BaseModel):
    origin: str
    destination: str
    distance: float
    distance_unit: str


class DistanceResponse(DistanceBase):
    pass
