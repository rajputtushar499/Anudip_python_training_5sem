# Question 2: Flight Booking Analysis Problem Statement
# A flight reservation system stores passenger records as tuples:
# bookings = (   
#   ("P101", "Delhi", "Confirmed"),   
#   ("P102", "Mumbai", "Waiting"),  
#   ("P103", "Delhi", "Confirmed"), 
#   ("P104", "Chennai", "Cancelled"), 
#   ("P105", "Mumbai", "Confirmed"), 
#   ("P106", "Delhi", "Waiting")
# )
# Where: 
# • Passenger ID
# • Destination 
# • Booking Status
# Tasks
# Write a Python program to:
# 1. Display all passengers whose booking status is Confirmed. 
# 2. Count the number of passengers travelling to Delhi.
# 3. Count Confirmed, Waiting, and Cancelled bookings separately. 
# 4. Create a list containing passenger IDs with Waiting status. 
# 5. Determine which destination has the highest number of bookings.
# Sample Output 
# Confirmed Passengers:
# P101 Delhi
# P103 Delhi 
# P105 Mumbai 
# Passengers Travelling to Delhi:3  
# Confirmed: 3
# Waiting: 2 
# Cancelled: 1  
# Waiting List:
# ['P102', 'P106']  
# Most Booked Destination: Delhi 
# Flight booking records stored in a tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display Confirmed Passengers
print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

# 2. Count passengers travelling to Delhi
delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count booking statuses
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# 4. Create waiting list
waiting_list = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])

print("\nWaiting List:", waiting_list)

# 5. Find most booked destination
destination_count = {}

for booking in bookings:
    destination = booking[1]

    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

most_booked = max(destination_count, key=destination_count.get)

print("\nMost Booked Destination:", most_booked)
