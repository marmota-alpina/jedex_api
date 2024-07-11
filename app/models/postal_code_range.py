from typing import Any

from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship

from app.core.database import Base


class PostalCodeRange(Base):
    __tablename__ = "postal_code_ranges"

    id = Column(String, primary_key=True, index=True)
    contract_id = Column(String, ForeignKey("contracts.id"), index=True)
    start_postal_code = Column(String, index=True, nullable=False)
    end_postal_code = Column(String, index=True, nullable=False)
    delivery_rate_per_kg = Column(Float, nullable=False)

    contract = relationship("Contract", back_populates="postal_code_ranges")

    def __init__(self, postal_code_range_id: str, contract_id: str, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = postal_code_range_id
        self.contract_id = contract_id
