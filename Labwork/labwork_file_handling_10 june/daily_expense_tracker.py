# TASK 1
# Read expenses from file

expenses = {}

try:
    file = open("expenses.txt", "r")

    for line in file:
        category, amount = line.strip().split(",")
        expenses[category] = int(amount)

    file.close()

except FileNotFoundError:
    print("File not found")


while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Highest and Lowest Spending")
    print("4. Display Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Summary Report")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    # TASK 2
    # Display all expenses
    if choice == 1:
        print("\nAll Expenses:")
        for category, amount in expenses.items():
            print(category, "-", amount)

    # TASK 3
    # Calculate total expenditure
    elif choice == 2:
        total = sum(expenses.values())
        print("Total Expenditure =", total)

    # TASK 4
    # Find highest and lowest spending category
    elif choice == 3:
        highest = max(expenses, key=expenses.get)
        lowest = min(expenses, key=expenses.get)

        print("Highest Spending Category:", highest, "-", expenses[highest])
        print("Lowest Spending Category:", lowest, "-", expenses[lowest])

    # TASK 5
    # Display expenses greater than ₹800
    elif choice == 4:
        print("\nExpenses Greater Than ₹800:")

        for category, amount in expenses.items():
            if amount > 800:
                print(category, "-", amount)

    # TASK 6
    # Add new expense category
    elif choice == 5:
        category = input("Enter category name: ")
        amount = int(input("Enter amount: "))

        expenses[category] = amount
        print("Expense category added successfully")

    # TASK 7
    # Update existing expense amount
    elif choice == 6:
        category = input("Enter category name: ")

        if category in expenses:
            new_amount = int(input("Enter new amount: "))
            expenses[category] = new_amount
            print("Expense updated successfully")
        else:
            print("Category not found")

    # TASK 8
    # Generate summary report in report.txt
    elif choice == 7:

        total = sum(expenses.values())

        highest = max(expenses, key=expenses.get)
        lowest = min(expenses, key=expenses.get)

        report = open("report.txt", "w")

        report.write("SUMMARY REPORT\n")
        report.write("------------------------\n")
        report.write("Total Expenses: " + str(total) + "\n")
        report.write("Highest Expense Category: " + highest + " = " + str(expenses[highest]) + "\n")
        report.write("Lowest Expense Category: " + lowest + " = " + str(expenses[lowest]) + "\n")

        report.write("\nCategories Spending More Than ₹800:\n")

        for category, amount in expenses.items():
            if amount > 800:
                report.write(category + " = " + str(amount) + "\n")

        report.close()

        print("Report generated successfully in report.txt")

    # TASK 9
    # Exit program
    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
