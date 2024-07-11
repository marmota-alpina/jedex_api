from typing import Any

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base


class Company(Base):
    __tablename__ = "companies"

    def __init__(self, company_id: str | None, **kw: Any):
        super().__init__(**kw)
        self.id = company_id
        self.active = True

    id = Column(String, primary_key=True, index=True)
    register_number = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)
    active = Column(Boolean, default=True)
    contracts = relationship("Contract", back_populates="company")
