from enum import Enum


class ShipmentType(str, Enum):
    ground = "ground"  # Ground shipping
    air = "air"  # Air shipping
    sea = "sea"  # Sea shipping


class OrderStatus(str, Enum):
    pending = "pending"  # Waiting for shipping
    shipped = "shipped"  # Order has been shipped
    delivered = "delivered"  # Order has been delivered
    cancelled = "cancelled"  # Order has been cancelled


class DurationUnit(str, Enum):
    hours = "hours"
    days = "days"
    weeks = "weeks"
    months = "months"


class DistanceUnit(str, Enum):
    km = "km"
    miles = "miles"


class WeightUnit(str, Enum):
    kg = "kg"
