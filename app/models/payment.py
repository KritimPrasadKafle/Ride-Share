

import enum
import uuid
from decimal import Decimal

from sqlalchemy import Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class PaymentStatus(str, enum.Enum):
    PENDING    = "PENDING"      # trip completed, payment not processed yet
    PROCESSING = "PROCESSING"   # being charged
    COMPLETED  = "COMPLETED"    # successful
    FAILED     = "FAILED"       # charge failed
    REFUNDED   = "REFUNDED"     # refund issued


class PaymentMethod(str, enum.Enum):
    CASH   = "CASH"    
    ESEWA  = "ESEWA"   
    KHALTI = "KHALTI"  
    CARD   = "CARD"


class Payment(BaseModel):
    __tablename__ = "payments"

    # ── References ─────────────────────────────────────
    trip_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("trips.id", ondelete="RESTRICT"),
        unique=True,    # one payment per trip
        nullable=False,
        index=True,
    )
    rider_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("riders.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    driver_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("drivers.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # ── Amounts ────────────────────────────────────────
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    # platform takes 20%, driver gets 80%
    driver_payout: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    platform_fee: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(
        String(3), default="NPR", nullable=False   # Nepali Rupee
    )

    # ── State ──────────────────────────────────────────
    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus),
        default=PaymentStatus.PENDING,
        nullable=False,
        index=True,
    )
    method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod),
        default=PaymentMethod.CASH,
        nullable=False,
    )

    # ── External reference ─────────────────────────────
    # eSewa/Khalti transaction ID — null for cash payments
    transaction_id: Mapped[str | None] = mapped_column(
        String(255), nullable=True, index=True
    )
    failure_reason: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Payment {self.trip_id} [{self.status}] NPR {self.amount}>"