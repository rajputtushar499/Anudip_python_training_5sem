# Employee details
name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Salary: "))

# Calculate salary components
hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

# Gross salary
gross = basic + hra + da

# Net salary
net = gross - pf

# Grade calculation
if net > 50000:
    grade = "Senior Grade"

elif net > 30000:
    grade = "Mid Grade"

else:
    grade = "Junior Grade"

# Display details
print("Employee Name:", name)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Grade:", grade)
