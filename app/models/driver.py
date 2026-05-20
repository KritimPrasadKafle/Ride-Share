from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, TIMESTAMP, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from enum import Enum

class DriverStatus(str, enum.Enum):
    AVAILABLE = 'available'
    ON_TRIP = 'on_trip'
    OFFLINE = 'offline'

class Driver(Base):
    __tablename__ = "drivers"
    __table_args__ = (
        CheckConstraint('rating >= 1.00 AND rating <= 5.00', name='driver_rating_range_check'),
        CheckConstraint('acceptannce_rate >= 0 AND acceptance_rate <= 100', name='acceptance_rate_range_check'),
    )
    

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    profile_picture_url: Mapped[str] = mapped_column(String(255), nullable=True)
    fcm_token: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    fcm_token: Mapped[str] = mapped_column(String(255), nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    license_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    status: Mapped[DriverStatus] = mapped_column(String(20), default=DriverStatus.AVAILABLE, nullable=False)

    current_latitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    current_longitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    rating: Mapped[float] = mapped_column(Numeric(3, 2), default=Decimal('5.0'), nullable=False)
    rating: Mapped[float] = mapped_column(Numeric(3, 2), default=Decimal('5.0'), nullable=False)
    total_trips: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    acceptance_rate: Mapped[float] = mapped_column(Numeric(5, 2), default=Decimal('100.00'), nullable=False)
    total_earnings: Mapped[float] = mapped_column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)

    def __repr__(self):
        return f"<Driver(id={self.id}, email='{self.email}', name='{self.name}')>"
