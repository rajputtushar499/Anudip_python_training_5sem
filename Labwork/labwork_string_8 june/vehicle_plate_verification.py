# Problem Statement
# A vehicle number plate is entered:
# MH12AB4589
# Tasks
# Write a program to:
# 1.Extract state code.
# 2.Extract district code.
# 3.Extract vehicle series.
# 4.Extract vehicle number.
# 5.Count letters and digits separately.
# 6.Verify:
# oFirst 2 characters must be alphabets.
# oNext 2 must be digits.
# oNext 2 must be alphabets.
# oLast 4 must be digits.
# 7.Display whether the number plate is valid.
# Sample Output
# Vehicle Number: MH12AB4589
# State Code: MH 
# District Code: 12
# Series: AB 
# Vehicle Number: 4589 
# Total Letters: 4 
# Total Digits: 6 
# Vehicle Number Status: Valid

# Vehicle Number Plate Verification

vehicle = "MH12AB4589"

# Task 1: Extract state code
state_code = vehicle[:2]
print("State Code:", state_code)

# Task 2: Extract district code
district_code = vehicle[2:4]
print("District Code:", district_code)

# Task 3: Extract vehicle series
series = vehicle[4:6]
print("Series:", series)

# Task 4: Extract vehicle number
vehicle_number = vehicle[6:]
print("Vehicle Number:", vehicle_number)

# Task 5: Count letters and digits separately
letters = 0
digits = 0

for ch in vehicle:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Total Letters:", letters)
print("Total Digits:", digits)

# Task 6 & 7: Verify number plate format

if (vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:6].isalpha() and
    vehicle[6:].isdigit() and
    len(vehicle) == 10):

    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")
