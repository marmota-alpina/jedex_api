from sqlalchemy import Column, String, Float, DateTime

from app.core.database import Base


class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(String, primary_key=True, index=True)
    company_id = Column(String, index=True)
    contract_id = Column(String, index=True)
    order_number = Column(String, index=True)

    weight = Column(Float)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)
    shipment_type = Column(String)

    origin_street = Column(String)
    origin_city = Column(String)
    origin_state = Column(String)
    origin_postal_code = Column(String, index=True)

    destination_name = Column(String, index=True)
    destination_street = Column(String, index=True)
    destination_city = Column(String, index=True)
    destination_state = Column(String, index=True)
    destination_postal_code = Column(String, index=True)
    destination_phone = Column(String, index=True)
    destination_email = Column(String, index=True)

    ship_date = Column(DateTime)
    delivery_date = Column(DateTime)
    delivery_status = Column(String, index=True)
    estimated_shipment_date = Column(DateTime)
    estimated_delivery_date = Column(DateTime)

    created_at = Column(DateTime)
