# List of bus seats
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Count booked seats
booked = seats.count(1)

# Count available seats
available = seats.count(0)

# Find first available seat
first_available = 0

for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1   # Seat number starts from 1
        break                     # Stop searching

# List of all available seat numbers
available_seats = []

for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

# Calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# Display results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

# Check occupancy status
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
