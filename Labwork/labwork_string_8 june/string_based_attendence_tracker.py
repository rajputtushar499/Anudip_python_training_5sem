# String-Based Attendance Tracker
# Problem Statement
# Attendance of a student for 15 days is represented as:
# PPAPPPAAPPPPAPP
# Where:
# •P = Present
# •A = Absent
# Tasks
# Write a program to:
# 1.Count Present and Absent days.
# 2.Calculate attendance percentage.
# 3.Find the longest consecutive streak of Presence.
# 4.Find the longest consecutive streak of Absence.
# 5.Determine whether attendance is below 75%.
# Sample Output
# Attendance Record: PPAPPPAAPPPPAPP
# Present Days: 11
# Absent Days: 4 
# Attendance Percentage: 73.33%
# Longest Present Streak: 4 
# Longest Absent Streak: 2
# Attendance Status: Below 75%

# String-Based Attendance Tracker

attendance = "PPAPPPAAPPPPAPP"

# Task 1: Count Present and Absent days
present = attendance.count("P")
absent = attendance.count("A")

print("Present Days:", present)
print("Absent Days:", absent)

# Task 2: Calculate attendance percentage
percentage = (present / len(attendance)) * 100
print("Attendance Percentage:", percentage)

# Task 3: Longest Present Streak
current_p = 0    #how many continuous "P" (Present) have come so far
longest_p = 0    #the longest present streak recorded so far

for ch in attendance:
    if ch == "P":
        current_p += 1
        if current_p > longest_p:
            longest_p = current_p
    else:
        current_p = 0

print("Longest Present Streak:", longest_p)

# Task 4: Longest Absent Streak
current_a = 0
longest_a = 0

for ch in attendance:
    if ch == "A":
        current_a += 1
        if current_a > longest_a:
            longest_a = current_a
    else:
        current_a = 0

print("Longest Absent Streak:", longest_a)

# Task 5: Check attendance status
if percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Above 75%")
