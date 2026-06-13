#  Student Attendance Percentage Calculator 
# Problem Statement 
# The attendance status of a student for 15 days is represented as follows: 
# Sample Data 
# attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
# Tasks 
# 1. Count present days.  
# 2. Count absent days.  
# 3. Calculate attendance percentage.  
# 4. Determine whether attendance is below 75%.  
# 5. Display the attendance status.  
# Sample Output 
# Present Days: 11 
 
# Absent Days: 4 
 
# Attendance Percentage: 73.33% 
 
# Attendance Status: 
# Below 75% 

#--------------------------------------------------
# Task 1: Count Present Days
#--------------------------------------------------

attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

present_days = attendance.count('P')

print("Present Days:", present_days)


#--------------------------------------------------
# Task 2: Count Absent Days
#--------------------------------------------------

absent_days = attendance.count('A')

print("\nAbsent Days:", absent_days)


#--------------------------------------------------
# Task 3: Calculate Attendance Percentage
#--------------------------------------------------

total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

print("\nAttendance Percentage: {:.2f}%".format(attendance_percentage))


#--------------------------------------------------
# Task 4: Determine Whether Attendance is Below 75%
#--------------------------------------------------

status = attendance_percentage < 75


#--------------------------------------------------
# Task 5: Display Attendance Status
#--------------------------------------------------

print("\nAttendance Status:")

if status:
    print("Below 75%")
else:
    print("75% or Above")
