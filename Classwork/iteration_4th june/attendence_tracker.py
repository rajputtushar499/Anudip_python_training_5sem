present = 0
absent = 0

student = 1

while student <= 30:
    attendance = input("Student " + str(student) + " Attendance (P/A): ")

    if attendance == "P":
        present += 1
    else:
        absent += 1

    student += 1

print("No. of Students Present :", present)
print("No. of Students Absent :", absent)
