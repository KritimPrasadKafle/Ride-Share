
from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column   

from app.models.base import Base

class Rider(Base):
    __tablename__ = 'riders'
    __table_args__ = (
        CheckConstraint('rating >= 1.00 AND rating <= 5.00', name='rating_range_check'),
    )

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    profile_picture_url: Mapped[str] = mapped_column(String(255), nullable=True)
    fcm_token: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    rating: Mapped[float] = mapped_column(Numeric(3, 2), default=Decimal('5.0'), nullable=False)
    total_trips: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    def __repr__(self):
        return f"<Rider(id={self.id}, email='{self.email}', name='{self.name}')>"


