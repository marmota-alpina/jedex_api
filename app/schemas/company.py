from typing import Optional

from pydantic import BaseModel, EmailStr


class CompanyBase(BaseModel):
    register_number: str
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    phone: str
    email: EmailStr


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    register_number: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


class CompanyResponse(CompanyBase):
    id: str
