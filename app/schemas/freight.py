from pydantic import BaseModel, Field

from app.core.constants import TRANSPORT_DURATION_DEFAULT
from app.core.enums import ShipmentType, DurationUnit
from app.schemas.dimension import DimensionModel
from app.schemas.distance import DistanceBase


class FreightRequest(BaseModel):
    contract_id: str
    origin_postal_code: str
    destination_postal_code: str
    weight: float
    dimensions: DimensionModel
    shipment_type: ShipmentType


class FreightResponse(BaseModel):
    shipment_type: ShipmentType = Field(ShipmentType.ground, alias='shipment_type')
    freight_cost: float
    duration: int = Field(TRANSPORT_DURATION_DEFAULT, alias='duration')
    chargeable_weight: float
    weight_unit: str = Field('kg', alias='weight_unit')
    duration_unit: DurationUnit = Field(DurationUnit.days, alias='duration_unit')
    distance: DistanceBase
