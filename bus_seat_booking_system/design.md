# Bus Seat Booking System — LLD Design

## 1. Enums

### SeatStatus
- AVAILABLE
- BOOKED

### BookingStatus
- CONFIRMED
- CANCELLED

## 2. Seat

**Attributes**
- `id: int`
- `status: SeatStatus`

**Responsibilities**
- Maintain seat availability.
- Change seat status when booked or released.

## 3. Bus

**Attributes**
- `id: int`
- `name: str`
- `source: str`
- `destination: str`
- `total_seats: int`
- `base_fare: float`
- `seats: list[Seat]`

**Relationships**
- One Bus contains multiple Seat objects.

**Responsibilities**
- Maintain its seats.
- Find a seat using its ID.
- Return available seats.
- Display seat availability.

## 4. Passenger

**Attributes**
- `id: int`
- `name: str`
- `email: str`
- `phone: str`
- `bookings: list[Booking]`

**Relationships**
- One Passenger can have multiple Bookings.

**Responsibilities**
- Maintain passenger information.
- Maintain booking history.

## 5. Booking

**Attributes**
- `id: int`
- `passenger: Passenger`
- `bus: Bus`
- `seats: list[Seat]`
- `total_fare: float`
- `status: BookingStatus`
- `booking_time: datetime`
- `cancellation_time: datetime | None`

**Relationships**
- Each Booking belongs to one Passenger.
- Each Booking belongs to one Bus.
- Each Booking contains one or more Seats.

**Responsibilities**
- Maintain booking details.
- Maintain booking status.
- Track booking and cancellation timestamps.

## 6. BookingService

**Attributes**
- `bookings: dict[int, Booking]`

**Methods**
- `book_seats(passenger_id, bus_id, seat_ids)`
- `cancel_booking(passenger_id, booking_id)`
- `get_booking(booking_id)`
- `get_booking_history(passenger_id)`
- `calculate_fare(bus, seats)`

**Responsibilities**
- Handle booking operations.
- Validate seat availability.
- Prevent duplicate seat bookings.
- Handle cancellation.
- Calculate total fare.
- Maintain booking records.

## 7. BookingManager

**Attributes**
- `buses: dict[int, Bus]`
- `passengers: dict[int, Passenger]`
- `booking_service: BookingService`

**Methods**
- `add_bus(bus)`
- `add_passenger(passenger)`
- `get_bus(bus_id)`
- `get_passenger(passenger_id)`
- `get_available_seats(bus_id)`
- `get_booking_statistics()`

**Responsibilities**
- Manage buses and passengers.
- Coordinate access to BookingService.
- Provide overall system operations.
- Generate booking statistics.

## 8. Business Rules

1. A passenger cannot book an already-booked seat.
2. A passenger cannot cancel another passenger's booking.
3. Cancelling a booking releases all associated seats.
4. Cancelled bookings must remain in booking history.
5. Invalid IDs and booking requests must be handled.
6. A booking must contain at least one seat.
7. Total fare = Number of seats × Bus base fare.
8. Only confirmed bookings can be cancelled.

## 9. Expected Operations

1. Register buses.
2. Register passengers.
3. Display available seats for a bus.
4. Book one or more seats.
5. View booking details.
6. Cancel a booking.
7. View passenger booking history.
8. Display bus seat availability.
9. Display booking statistics.

