from pydantic import BaseModel


class PostalCodeRangeBase(BaseModel):
    start_postal_code: str
    end_postal_code: str
    delivery_rate_per_kg: float


class PostalCodeRangeCreate(PostalCodeRangeBase):
    pass


class PostalCodeRangeUpdate(PostalCodeRangeBase):
    pass


class PostalCodeRange(PostalCodeRangeBase):
    id: str
    contract_id: str

    class Config:
        orm_mode = True
