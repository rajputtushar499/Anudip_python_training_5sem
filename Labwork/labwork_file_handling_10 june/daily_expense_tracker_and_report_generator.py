#  Daily Expense Tracker and Report Generator 
# Problem Statement 
# Daily expenses are recorded in expenses.txt. 
# File Format 
# Food,450 
# Travel,300 
# Shopping,1200 
# Electricity,850 
# Internet,700 
# Entertainment,600 
# Medicine,400 
# Education,1500 
# Fuel,900 
# Miscellaneous,250 
# Requirements 
# Develop a program to: 
# 1. Display all expenses.  
# 2. Calculate total expenditure.  
# 3. Find the category with highest and lowest spending.  
# 4. Display expenses greater than ₹800.  
# 5. Add a new expense category.  
# 6. Update an existing expense amount.  
# 7. Generate a summary report in report.txt containing:  
# o Total Expenses  
# o Highest Expense Category  
# o Lowest Expense Category  
# o Categories spending more than ₹800 

#------------------------------------------------------------------------------------------
# Daily Expense Tracker and Report Generator

# --------------------------------------------------
# TASK 1 - Display All Expenses
# --------------------------------------------------

file = open("expenses.txt", "r")

print("All Expenses:")

for line in file:
    print(line.strip())

file.close()
print()

# --------------------------------------------------
# TASK 2 - Calculate Total Expenditure
# --------------------------------------------------

file = open("expenses.txt", "r")

total = 0

for line in file:
    data = line.strip().split(",")
    total = total + int(data[1])

file.close()

print("Total Expenditure: ₹", total)
print()

# --------------------------------------------------
# TASK 3 - Find Highest and Lowest Spending Category
# --------------------------------------------------

file = open("expenses.txt", "r")

highest_category = ""
lowest_category = ""

highest_amount = 0
lowest_amount = 99999

for line in file:

    data = line.strip().split(",")

    category = data[0]
    amount = int(data[1])

    if amount > highest_amount:
        highest_amount = amount
        highest_category = category

    if amount < lowest_amount:
        lowest_amount = amount
        lowest_category = category

file.close()

print("Highest Expense Category:")
print(highest_category, "-", highest_amount)

print("\nLowest Expense Category:")
print(lowest_category, "-", lowest_amount)
print()

# --------------------------------------------------
# TASK 4 - Display Expenses Greater Than ₹800
# --------------------------------------------------

file = open("expenses.txt", "r")

print("Expenses Greater Than ₹800:")

for line in file:

    data = line.strip().split(",")

    if int(data[1]) > 800:
        print(data[0], "-", data[1])

file.close()
print()

# --------------------------------------------------
# TASK 5 - Add New Expense Category
# --------------------------------------------------

category = input("Enter New Category: ")
amount = input("Enter Amount: ")

file = open("expenses.txt", "a")
file.write("\n" + category + "," + amount)
file.close()

print("New Expense Added Successfully.")
print()

# --------------------------------------------------
# TASK 6 - Update Existing Expense Amount
# --------------------------------------------------

update_category = input("Enter Category To Update: ")
new_amount = input("Enter New Amount: ")

file = open("expenses.txt", "r")
lines = file.readlines()
file.close()

file = open("expenses.txt", "w")

for line in lines:

    data = line.strip().split(",")

    if data[0] == update_category:
        file.write(data[0] + "," + new_amount + "\n")
    else:
        file.write(line)

file.close()

print("Expense Updated Successfully.")
print()

# --------------------------------------------------
# TASK 7 - Generate Summary Report in report.txt
# --------------------------------------------------

file = open("expenses.txt", "r")

total = 0
highest_amount = 0
lowest_amount = 99999

highest_category = ""
lowest_category = ""

more_than_800 = []

for line in file:

    data = line.strip().split(",")

    category = data[0]
    amount = int(data[1])

    total = total + amount

    if amount > highest_amount:
        highest_amount = amount
        highest_category = category

    if amount < lowest_amount:
        lowest_amount = amount
        lowest_category = category

    if amount > 800:
        more_than_800.append(category)

file.close()

report = open("report.txt", "w")

report.write("Total Expenses: " + str(total) + "\n")
report.write("Highest Expense Category: " + highest_category + "\n")
report.write("Lowest Expense Category: " + lowest_category + "\n")

report.write("Categories Spending More Than 800:\n")

for item in more_than_800:
    report.write(item + "\n")

report.close()

print("Summary Report Generated Successfully.")
