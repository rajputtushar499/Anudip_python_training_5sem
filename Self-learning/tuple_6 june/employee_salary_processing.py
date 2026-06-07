# Employee Salary Processing
# Sample Data
# salary = { 
# "EMP101": 45000, 
# "EMP102": 62000, 
# "EMP103": 38000, 
# "EMP104": 75000,
# "EMP105": 54000,
# "EMP106": 29000,
# "EMP107": 82000,
# "EMP108": 48000,
# "EMP109": 36000,
# "EMP110": 68000
# }
# Tasks
# Display employees earning above ₹60,000.
# Count employees earning below ₹40,000.
# Find the highest-paid employee.
# Create a list of employees eligible for a bonus (salary > ₹50,000).
# Calculate the average salary.

# Employee Salary Dictionary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above 60000
print("Employees earning above 60000:")
for emp in salary:
    if salary[emp] > 60000:
        print(emp, salary[emp])

# Count employees earning below 40000
count = 0

for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("\nEmployees earning below 40000:", count)

# Find highest-paid employee
highest_salary = 0

for emp in salary:
    if salary[emp] > highest_salary:
        highest_salary = salary[emp]
        highest_emp = emp

print("Highest Paid Employee:")
print(highest_emp, highest_salary)

# Employees eligible for bonus
bonus_list = []

for emp in salary:
    if salary[emp] > 50000:
        bonus_list.append(emp)

print("\nEmployees eligible for bonus:")
print(bonus_list)

# Calculate average salary
total = 0

for emp in salary:
    total += salary[emp]

average = total / len(salary)

print("\nAverage Salary:", average)
