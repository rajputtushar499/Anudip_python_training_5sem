# Employee Dictionary (10 Employees)
employees = {}
# Input data
for i in range(10):
    emp_id = input("Enter Employee ID: ")
    salary = int(input("Enter Salary: "))
    employees[emp_id] = salary

# Count salary > 30000
count = 0

print("\nEmployees with salary below 20000:")

for emp_id in employees:
    if employees[emp_id] > 30000:
        count += 1

    if employees[emp_id] < 20000:
        print("Employee ID:", emp_id, "Salary:", employees[emp_id])

print("\nTotal employees with salary greater than 30000:", count)
