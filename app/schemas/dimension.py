from pydantic import BaseModel


class DimensionModel(BaseModel):
    height: float
    width: float
    length: float
