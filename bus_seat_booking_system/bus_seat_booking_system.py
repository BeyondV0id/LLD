# Seat:
#   id: int
#   status: SeatStatus

# Bus:
#   id: int
#   name: str
#   source: str
#   destination: str
#   total_seats: int
#   base_fare: float
#   seats: list[Seat]

# Passenger:
#   id: int
#   name: str
#   email: str
#   phone: str
#   bookings: list[Booking]

# Booking:
#   id: int
#   passenger: Passenger
#   bus: Bus
#   seats: list[Seat]
#   total_fare: float
#   status: BookingStatus
#   booking_time: datetime
#   cancellation_time: datetime | None

# BookingService:
#   bookings: dict[int, Booking]
#
#   book_seats(passenger_id, bus_id, seat_ids)
#   cancel_booking(passenger_id, booking_id)
#   get_booking(booking_id)
#   get_booking_history(passenger_id)
#   calculate_fare(bus, seats)

# BookingManager:
#   buses: dict[int, Bus]
#   passengers: dict[int, Passenger]
#   booking_service: BookingService
#
#   add_bus(bus)
#   add_passenger(passenger)
#   get_bus(bus_id)
#   get_passenger(passenger_id)
#   get_available_seats(bus_id)
#   get_booking_statistics()
