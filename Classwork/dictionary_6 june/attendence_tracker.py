attendance = {}

for i in range(30):
    roll = input("Enter Roll Number: ")
    status = input("Enter P (Present) or A (Absent): ")
    attendance[roll] = status

print("\nPresent Students:")

for roll in attendance:
    if attendance[roll] == "P":
        print(roll)
