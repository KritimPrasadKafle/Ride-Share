import uuid
from sqlalchemy import String, ForeignKey, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.models.base import Base


class TripStatus(str, enum.Enum):
    REQUESTED = "requested"
    ACCEPTED = "accepted"
    STARTED = "started"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Trip(Base):
    __tablename__ = "trips"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    rider_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("riders.id"))
    driver_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("drivers.id"), nullable=True)

    pickup_location: Mapped[str] = mapped_column(String(255))
    drop_location: Mapped[str] = mapped_column(String(255))

    distance_km: Mapped[float] = mapped_column(Float, nullable=True)
    fare: Mapped[float] = mapped_column(Float, nullable=True)

    status: Mapped[TripStatus] = mapped_column(
        Enum(TripStatus),
        default=TripStatus.REQUESTED
    )