#  Employee Payroll Management System 
# Problem Statement 
# A company stores employee details in a text file named employees.txt. 
# File Format 
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
# Requirements 
# Create a menu-driven program to: 
# 1. Display all employee records.  
# 2. Search employee details using Employee ID.  
# 3. Calculate the average salary.  
# 4. Find the highest-paid and lowest-paid employee.  
# 5. Display employees earning above ₹50,000.  
# 6. Add a new employee record to the file.  
# 7. Generate salary categories:  
# o High (₹60,000 and above)  
# o Medium (₹40,000–₹59,999)  
# o Low (Below ₹40,000) 

# Employee Payroll Management System

while True:

    print("\n===== EMPLOYEE PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Display All Employee Records")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Highest Paid and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all employee records
    if choice == 1:

        file = open("employees.txt", "r")

        print("\nEmployee Records:")
        print(file.read())

        file.close()

    # 2. Search employee by ID
    elif choice == 2:

        emp_id = input("Enter Employee ID: ")

        file = open("employees.txt", "r")

        found = False

        for line in file:

            data = line.strip().split(",")

            if data[0] == emp_id:
                print("\nEmployee Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Salary:", data[2])

                found = True

        if found == False:
            print("Employee Not Found")

        file.close()

    # 3. Calculate average salary
    elif choice == 3:

        file = open("employees.txt", "r")

        total_salary = 0
        count = 0

        for line in file:

            data = line.strip().split(",")

            total_salary = total_salary + int(data[2])
            count = count + 1

        average = total_salary / count

        print("Average Salary =", average)

        file.close()

    # 4. Highest and Lowest paid employee
    elif choice == 4:

        file = open("employees.txt", "r")

        highest_salary = 0
        lowest_salary = 999999

        highest_name = ""
        lowest_name = ""

        for line in file:

            data = line.strip().split(",")

            salary = int(data[2])

            if salary > highest_salary:
                highest_salary = salary
                highest_name = data[1]

            if salary < lowest_salary:
                lowest_salary = salary
                lowest_name = data[1]

        print("Highest Paid Employee:", highest_name, "-", highest_salary)
        print("Lowest Paid Employee :", lowest_name, "-", lowest_salary)

        file.close()

    # 5. Employees earning above 50000
    elif choice == 5:

        file = open("employees.txt", "r")

        print("\nEmployees Earning Above 50000")

        for line in file:

            data = line.strip().split(",")

            if int(data[2]) > 50000:
                print(data[0], data[1], data[2])

        file.close()

    # 6. Add new employee
    elif choice == 6:

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        file = open("employees.txt", "a")

        file.write("\n" + emp_id + "," + name + "," + salary)

        file.close()

        print("Employee Added Successfully")

    # 7. Salary categories
    elif choice == 7:

        file = open("employees.txt", "r")

        print("\nSalary Categories")

        for line in file:

            data = line.strip().split(",")

            salary = int(data[2])

            if salary >= 60000:
                category = "High"

            elif salary >= 40000:
                category = "Medium"

            else:
                category = "Low"

            print(data[1], "-", category)

        file.close()

    # 8. Exit
    elif choice == 8:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")

