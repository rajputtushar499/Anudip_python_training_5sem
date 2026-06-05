# List of bus seats
# 1 = Booked Seat
# 0 = Available Seat
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Count booked and available seats
booked_seats = 0
available_seats = 0

for seat in seats:
    if seat == 1:
        booked_seats += 1
    else:
        available_seats += 1

# Find the first available seat
# Stop the loop as soon as an available seat is found
first_available_seat = -1

for i in range(len(seats)):
    if seats[i] == 0:
        first_available_seat = i + 1  # Seat numbering starts from 1
        break

# Store all available seat numbers in a list
available_seat_numbers = []

for i in range(len(seats)):
    if seats[i] == 0:
        available_seat_numbers.append(i + 1)

# Calculate bus occupancy percentage
occupancy = (booked_seats / len(seats)) * 100

# Display the output
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
print("First Available Seat:", first_available_seat)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", int(occupancy), "%")

# Check whether occupancy is more than 70%
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
