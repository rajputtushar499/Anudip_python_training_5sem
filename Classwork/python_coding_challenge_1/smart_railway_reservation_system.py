#  Smart Railway Reservation System 
# Problem Statement 
# A railway reservation system stores the booking status of seats in a train coach. 
# Sample Data 
# seats = { 
#     1: "Booked", 
#     2: "Available", 
#     3: "Booked", 
#     4: "Available", 
#     5: "Booked", 
#     6: "Booked", 
#     7: "Available", 
#     8: "Booked", 
#     9: "Available", 
#     10: "Booked" 
# } 
# Tasks 
# 1. Display all available seat numbers.  
# 2. Count booked and available seats.  
# 3. Reserve the first available seat.  
# 4. Cancel booking for a given seat number.  
# 5. Store the updated reservation status in reservations.txt.  
# 6. Display occupancy percentage.  
# Sample Output 
# Available Seats: 
# 2 4 7 9 
 
# Booked Seats: 6 
# Available Seats: 4 
 
# Seat 2 Reserved Successfully. 
 
# Occupancy Percentage: 70.0% 
 
# Reservation Details Saved Successfully. 

# Smart Railway Reservation System

# Smart Railway Reservation System

seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# TASK 1 - Display available seats
print("TASK 1 - Available Seats")
for seat in seats:
    if seats[seat] == "Available":
        print(seat, end=" ")
print("\n")


# TASK 2 - Count booked and available seats
print("TASK 2 - Count Seats")

booked = 0
available = 0

for seat in seats:
    if seats[seat] == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)
print()


# TASK 3 - Reserve first available seat
print("TASK 3 - Reserve First Available Seat")

for seat in seats:
    if seats[seat] == "Available":
        seats[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        break
print()


# TASK 4 - Cancel booking
print("TASK 4 - Cancel Booking")

seat_no = int(input("Enter Seat Number: "))

if seat_no in seats:
    seats[seat_no] = "Available"
    print("Booking Cancelled Successfully.")
else:
    print("Invalid Seat Number")
print()


# TASK 5 - Save reservation details in file
print("TASK 5 - Save Data")

file = open("reservations.txt", "w")

for seat in seats:
    file.write(str(seat) + "," + seats[seat] + "\n")

file.close()

print("Reservation Details Saved Successfully.")
print()


# TASK 6 - Occupancy Percentage
print("TASK 6 - Occupancy Percentage")

booked = 0

for seat in seats:
    if seats[seat] == "Booked":
        booked += 1

occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage:", occupancy, "%")
