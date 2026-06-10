# Train Reservation Waiting List
# Problem Statement
# Passenger records:
# passengers = [
# ("Anuj", "Confirmed"),
# ("Rahul", "Waiting"),
# ("Priya", "Confirmed"),
# ("Amit", "Waiting"),
# ("Neha", "Confirmed")
# ]
# Write a program to:
# * Display all waiting-list passengers.
# * Count confirmed and waiting passengers.
# * Find whether a specific passenger has a confirmed ticket.
# * Create separate lists for confirmed and waiting passengers.

# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# Task 1: Display all waiting-list passengers
print("Waiting List Passengers:")

for passenger in passengers:
    if passenger[1] == "Waiting":
        print(passenger[0])

# Task 2: Count confirmed and waiting passengers
for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Task 3: Find whether a specific passenger has a confirmed ticket
search_name = "Priya"

for passenger in passengers:
    if passenger[0] == search_name and passenger[1] == "Confirmed":
        print("\n", search_name, "has a Confirmed Ticket")
        break

# Task 4: Create separate lists for confirmed and waiting passengers
for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])
    else:
        waiting_list.append(passenger[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)
