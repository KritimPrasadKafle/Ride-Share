from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, TIMESTAMP, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from enum import Enum


class VehicleType(str, Enum):
    SEDAN = 'sedan'
    SUV = 'suv'
    HATCHBACK = 'hatchback'
    VAN = 'van'
    TRUCK = 'truck'
    BIKE = 'bike'

class Vehicle(Base):

    __tablename__ = 'vehicles'

    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey('drivers.id'), nullable=False)
    type: Mapped[VehicleType] = mapped_column(String(20), nullable=False)

    make: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    license_plate: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
    vehicle_type: Mapped[VehicleType] = mapped_column(String(20), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    driver = relationship("Driver", back_populates="vehicles")

    def __repr__(self):
        return f"<Vehicle(id={self.id}, make='{self.make}', model='{self.model}', license_plate='{self.license_plate}')>"