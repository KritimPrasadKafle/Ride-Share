

class TripStatus(str, Enum):
    REQUESTED = 'requested'
    DRIVER_ASSIGNED = 'driver_assigned'
    DRIVER_EN_ROUTE = 'driver_en_route'
    DRIVER_ARRIVED = 'driver_arrived'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    DISPUTED = 'disputed'
    PAID = 'paid'

VALID_TRANSITIONS : dict[TripStatus, list[TripStatus]] = {
    TripStatus.REQUESTED: [TripStatus.DRIVER_ASSIGNED, TripStatus.CANCELLED],
    TripStatus.DRIVER_ASSIGNED: [TripStatus.DRIVER_EN_ROUTE, TripStatus.CANCELLED],
    TripStatus.DRIVER_EN_ROUTE: [TripStatus.DRIVER_ARRIVED, TripStatus.CANCELLED],
    TripStatus.DRIVER_ARRIVED: [TripStatus.IN_PROGRESS, TripStatus.CANCELLED],
    TripStatus.IN_PROGRESS: [TripStatus.COMPLETED, TripStatus.CANCELLED],
    TripStatus.COMPLETED: [TripStatus.PAID, TripStatus.DISPUTED],
    TripStatus.CANCELLED: [],
    TripStatus.DISPUTED: [TripStatus.COMPLETED],
    TripStatus.PAID: []
}

class Trip(Base):
    __tablename__ = 'trips'
    
    rider_id: Mapped[int] = mapped_column(Integer, ForeignKey('riders.id'), nullable=False)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey('drivers.id'), nullable=True)

    pickup_latitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=False)
    pickup_longitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=False)
    pickup_address: Mapped[str] = mapped_column(String(255), nullable=True)

    dropoff_latitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=False)
    dropoff_longitude: Mapped[float] = mapped_column(Numeric(10, 6), nullable=False)
    dropoff_address: Mapped[str] = mapped_column(String(255), nullable=True)


    status: Mapped[TripStatus] = mapped_column(String(20), default=TripStatus.REQUESTED, nullable=False)
    cancel_reason: Mapped[str] = mapped_column(String(255), nullable=True)
    started_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    completed_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    vehicle_type: Mapped[VehicleType] = mapped_column(String(20), nullable=True)
    estimated_fare: Mapped[float] = mapped_column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)

    final_fare: Mapped[float] = mapped_column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)
    surge_multiplier: Mapped[float] = mapped_column(Numeric(3, 2), default=Decimal('1.00'), nullable=False)

    distance_km: Mapped[float] = mapped_column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)
    duration_minutes: Mapped[float] = mapped_column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)

    rider = relationship("Rider", back_populates="trips")
    driver = relationship("Driver", back_populates="trips")

    def __repr__(self):
        return f"<Trip(id={self.id}, rider_id={self.rider_id}, driver_id={self.driver_id}, status='{self.status}')>"