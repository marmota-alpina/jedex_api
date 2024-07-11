from datetime import datetime
from typing import Any
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

from app.core.constants import DIMENSIONAL_FACTOR_DEFAULT
from app.core.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(String, primary_key=True, index=True)
    company_id = Column(String, ForeignKey("companies.id"), index=True)
    start_date = Column(DateTime, index=True, nullable=False)
    end_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    dimensional_factor = Column(Float, nullable=True, default=DIMENSIONAL_FACTOR_DEFAULT)

    company = relationship("Company", back_populates="contracts")
    postal_code_ranges = relationship("PostalCodeRange", back_populates="contract")

    def __init__(self, contract_id: str, **kwargs: Any):
        super().__init__(**kwargs)
        self.id = contract_id
        self.active = True
