import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    driver_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("drivers.id"),
        nullable=False
    )

    plate_number: Mapped[str] = mapped_column(String(20), unique=True)
    model: Mapped[str] = mapped_column(String(50))