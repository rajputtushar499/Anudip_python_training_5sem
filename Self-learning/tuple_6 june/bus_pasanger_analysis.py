# Bus Route Passenger Analysis
# Sample Data
# passengers = { 
# "Stop1": 12, 
# "Stop2": 25, 
# "Stop3": 18,
# "Stop4": 32,
# "Stop5": 9, 
# "Stop6": 28,
# "Stop7": 14,
# "Stop8": 7, 
# "Stop9": 21,
# "Stop10": 16
# }
# Tasks
# Display stops having more than 20 passengers.
# Count stops with fewer than 10 passengers.
# Find the busiest stop.
# Create a list of stops requiring an extra bus (passengers > 25).
# Calculate the average number of passengers.

# Passenger Dictionary
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Stops having more than 20 passengers
print("Stops having more than 20 passengers:")
for stop in passengers:
    if passengers[stop] > 20:
        print(stop, passengers[stop])

# Count stops with fewer than 10 passengers
count = 0

for stop in passengers:
    if passengers[stop] < 10:
        count += 1

print("Stops with fewer than 10 passengers:", count)

# Find busiest stop
max_passengers = 0

for stop in passengers:
    if passengers[stop] > max_passengers:
        max_passengers = passengers[stop]
        max_stop = stop

print("Busiest Stop:")
print(max_stop, max_passengers)

# Stops requiring an extra bus
extra_bus = []

for stop in passengers:
    if passengers[stop] > 25:
        extra_bus.append(stop)

print("Stops requiring an extra bus:")
print(extra_bus)

# Calculate average passengers
total = 0

for stop in passengers:
    total += passengers[stop]

average = total / len(passengers)

print("Average Number of Passengers:", average)
