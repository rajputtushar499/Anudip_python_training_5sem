present = 0
absent = 0

i = 1

while i <= 30:
    status = input("Enter P for Present and A for Absent: ")

    if status == "P":
        present += 1
    else:
        absent += 1

    i += 1

print("Present Students =", present)
print("Absent Students =", absent)
