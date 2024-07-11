from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from app.core.constants import DIMENSIONAL_FACTOR_DEFAULT
from app.schemas.postal_code_range import PostalCodeRangeCreate


class ContractBase(BaseModel):
    company_id: str
    start_date: datetime
    end_date: datetime


class ContractCreate(ContractBase):
    dimensional_factor: Optional[float] = DIMENSIONAL_FACTOR_DEFAULT
    ranges: Optional[List[PostalCodeRangeCreate]] = None


class ContractUpdate(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    ranges: Optional[List[PostalCodeRangeCreate]] = None


class Contract(ContractBase):
    id: str
    is_active: bool = Field(False, alias='active', serialization_alias='is_active')
    created_at: datetime
    dimensional_factor: float = Field(DIMENSIONAL_FACTOR_DEFAULT, alias='dimensional_factor')
    ranges: Optional[List[PostalCodeRangeCreate]] = Field(None, alias='postal_code_ranges',
                                                          serialization_alias='ranges')

    class Config:
        orm_mode = True
