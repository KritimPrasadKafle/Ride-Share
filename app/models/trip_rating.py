import uuid
from decimal import Decimal

from sqlalchemy import CheckConstraint, ForeignKey, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel



class TripRating(BaseModel):
    __tablename__ = "trip_ratings"
    __table_args__ = (
        # Numeric(2,1) allows 1.0–5.0. Constraint ensures no out-of-range values.
        CheckConstraint(
            "driver_rating IS NULL OR (driver_rating >= 1.0 AND driver_rating <= 5.0)",
            name="ck_driver_rating_range",
        ),
        CheckConstraint(
            "rider_rating IS NULL OR (rider_rating >= 1.0 AND rider_rating <= 5.0)",
            name="ck_rider_rating_range",
        ),
    )

    trip_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("trips.id", ondelete="CASCADE"),
        unique=True,    # one rating record per trip
        nullable=False,
        index=True,
    )

    # ── Rider rates the driver ─────────────────────────
    driver_rating: Mapped[Decimal | None] = mapped_column(
        Numeric(2, 1), nullable=True    # e.g. 4.5
    )
    driver_feedback: Mapped[str | None] = mapped_column(Text, nullable=True)

    # ── Driver rates the rider ─────────────────────────
    rider_rating: Mapped[Decimal | None] = mapped_column(
        Numeric(2, 1), nullable=True
    )
    rider_feedback: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<TripRating trip={self.trip_id}>"