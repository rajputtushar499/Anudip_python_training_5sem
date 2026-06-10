# Employee Salary Processing
# Problem Statement
# Employee data is stored as tuples:
# employees = [
# ("Rahul", 35000),
# ("Priya", 55000),
# ("Amit", 42000),
# ("Neha", 65000)
# ]
# Write a program to:
# * Display employees earning above ₹50,000.
# * Find the highest-paid employee.
# * Calculate total salary expenditure.
# * Count employees earning below ₹40,000.
# Employee names and salaries
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Display employees earning above 50000
print("Employees earning above 50000:")

for emp in employees:
    if emp[1] > 50000:
        print(emp[0], emp[1])

# Find highest-paid employee
highest = employees[0]  # Assume first employee has highest salary

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("\nHighest Paid Employee:")
print(highest[0], highest[1])

# Calculate total salary expenditure
total = 0

for emp in employees:
    total += emp[1]

print("\nTotal Salary Expenditure:", total)

# Count employees earning below 40000
count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("\nEmployees earning below 40000:", count)
