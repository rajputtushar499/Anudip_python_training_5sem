#  Student Result Processing System 
# Problem Statement 
# Student marks are stored in results.txt. 
# File Format 
# S101,Anuj,85 
# S102,Rahul,72 
# S103,Priya,96 
# S104,Neha,68 
# S105,Amit,39 
# S106,Sneha,54 
# S107,Karan,91 
# S108,Pooja,78 
# S109,Rohit,47 
# S110,Anjali,88 
# Requirements 
# Write a program to: 
# 1. Display all student records.  
# 2. Search a student using Student ID.  
# 3. Find topper and lowest scorer.  
# 4. Calculate class average.  
# 5. Count pass and fail students.  
# 6. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (40–74)  
# o F (<40)  
# 7. Write grade reports into a new file named grades.txt. 

# Student Result Processing System

while True:

    print("\n===== STUDENT RESULT PROCESSING SYSTEM =====")
    print("1. Display All Student Records")
    print("2. Search Student by ID")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades")
    print("7. Create grades.txt File")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all student records
    if choice == 1:

        file = open("results.txt", "r")
        print(file.read())
        file.close()

    # 2. Search student by ID
    elif choice == 2:

        sid = input("Enter Student ID: ")

        file = open("results.txt", "r")

        found = False

        for line in file:

            data = line.strip().split(",")

            if data[0] == sid:

                print("ID    :", data[0])
                print("Name  :", data[1])
                print("Marks :", data[2])

                found = True

        if found == False:
            print("Student Not Found")

        file.close()

    # 3. Topper and Lowest Scorer
    elif choice == 3:

        file = open("results.txt", "r")

        highest = 0
        lowest = 100

        topper = ""
        low_student = ""

        for line in file:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks > highest:
                highest = marks
                topper = data[1]

            if marks < lowest:
                lowest = marks
                low_student = data[1]

        print("Topper :", topper, "-", highest)
        print("Lowest Scorer :", low_student, "-", lowest)

        file.close()

    # 4. Calculate average
    elif choice == 4:

        file = open("results.txt", "r")

        total = 0
        count = 0

        for line in file:

            data = line.strip().split(",")

            total = total + int(data[2])
            count = count + 1

        print("Class Average =", total / count)

        file.close()

    # 5. Count pass and fail students
    elif choice == 5:

        file = open("results.txt", "r")

        pass_count = 0
        fail_count = 0

        for line in file:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 40:
                pass_count += 1
            else:
                fail_count += 1

        print("Pass Students :", pass_count)
        print("Fail Students :", fail_count)

        file.close()

    # 6. Generate grades
    elif choice == 6:

        file = open("results.txt", "r")

        print("\nStudent Grades")

        for line in file:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "F"

            print(data[1], "-", grade)

        file.close()

    # 7. Write grades into grades.txt
    elif choice == 7:

        file = open("results.txt", "r")
        grade_file = open("grades.txt", "w")

        for line in file:

            data = line.strip().split(",")

            marks = int(data[2])

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "F"

            grade_file.write(data[0] + "," + data[1] + "," + grade + "\n")

        file.close()
        grade_file.close()

        print("grades.txt created successfully")

    # 8. Exit
    elif choice == 8:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")

