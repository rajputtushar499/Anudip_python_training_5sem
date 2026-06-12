# Employee Salary Report Generator 
# Problem Statement 
# Employee details are stored in a text file named employees.txt. 
# Sample Input/Data (employees.txt) 
# EMP101,Anuj,45000 
# EMP102,Rahul,52000 
# EMP103,Priya,38000 
# EMP104,Neha,61000 
# EMP105,Amit,29000 
# EMP106,Sneha,55000 
# EMP107,Karan,47000 
# EMP108,Pooja,72000 
# EMP109,Rohit,33000 
# EMP110,Anjali,68000 
# Tasks 
# 1. Display employees earning more than ₹50,000.  
# 2. Find the highest-paid employee.  
# 3. Find the lowest-paid employee.  
# 4. Calculate the average salary.  
# 5. Generate salary categories:  
# o High (≥ ₹60,000)  
# o Medium (₹40,000 – ₹59,999)  
# o Low (< ₹40,000)  
# Sample Output 
# Employees Earning Above ₹50,000: 
# Rahul 
# Neha 
# Sneha 
# Pooja 
# Anjali 
 
# Highest Paid Employee: 
# Pooja (₹72,000) 
 
# Lowest Paid Employee: 
# Amit (₹29,000) 
 
# Average Salary: ₹50,000 
 
# High Salary: 
# ['Neha', 'Pooja', 'Anjali'] 
 
# Medium Salary: 
# ['Anuj', 'Rahul', 'Sneha', 'Karan'] 
 
# Low Salary: 
# ['Priya', 'Amit', 'Rohit']

#----------------------------------------------------

# employees.txt
# EMP101,Anuj,45000
# EMP102,Rahul,52000
# EMP103,Priya,38000
# EMP104,Neha,61000
# EMP105,Amit,29000
# EMP106,Sneha,55000
# EMP107,Karan,47000
# EMP108,Pooja,72000
# EMP109,Rohit,33000
# EMP110,Anjali,68000

#----------------------------------------------------

# Employee Salary Report Generator

#----------------------------------------------------

file = open("employees.txt", "r")
lines = file.readlines()
file.close()

#-----------------------------------------------------
# Task 1
#-----------------------------------------------------

print("Employees Earning Above ₹50,000:")

for line in lines:
    data = line.strip().split(",")

    name = data[1]
    salary = int(data[2])

    if salary > 50000:
        print(name)

#-------------------------------------------------------
# Task 2
#-------------------------------------------------------

highest_salary = 0

for line in lines:
    data = line.strip().split(",")

    name = data[1]
    salary = int(data[2])

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

print("\nHighest Paid Employee:")
print(highest_employee, "(", highest_salary, ")")

#-------------------------------------------------------
# Task 3
#-------------------------------------------------------

lowest_salary = 100000
lowest_employee = ""

for line in lines:
    data = line.strip().split(",")

    name = data[1]
    salary = int(data[2])

    if salary < lowest_salary:
        lowest_salary = salary
        lowest_employee = name

print("\nLowest Paid Employee:")
print(lowest_employee, "(", lowest_salary, ")")

#----------------------------------------------------
# Task 4
#----------------------------------------------------

total = 0

for line in lines:
    data = line.strip().split(",")

    salary = int(data[2])

    total = total + salary

average = total / len(lines)

print("\nAverage Salary:")
print(average)

#-------------------------------------------------------
# Task 5
#-------------------------------------------------------

high = []
medium = []
low = []

for line in lines:
    data = line.strip().split(",")

    name = data[1]
    salary = int(data[2])

    if salary >= 60000:
        high.append(name)

    elif salary >= 40000:
        medium.append(name)

    else:
        low.append(name)

print("High Salary:")
print(high)

print("Medium Salary:")
print(medium)

print("Low Salary:")
print(low)
