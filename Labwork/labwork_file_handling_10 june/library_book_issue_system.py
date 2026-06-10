#  Library Book Issue System 
# Problem Statement 
# A library stores book information in books.txt. 
# File Format 
# B101,Python Basics,5 
# B102,Java Programming,2 
# B103,Data Science,0 
# B104,DBMS,3 
# B105,Machine Learning,1 
# B106,Operating Systems,4 
# B107,Networking,2 
# B108,Cyber Security,6 
# B109,Cloud Computing,0 
# B110,Web Development,3 
# Requirements 
# Develop a program to: 
# 1. Display all books.  
# 2. Search a book using Book ID.  
# 3. Issue a book (decrease quantity by 1).  
# 4. Return a book (increase quantity by 1).  
# 5. Display unavailable books.  
# 6. Display books requiring restocking (copies < 2).  
# 7. Update the file after every issue/return operation. 

# Library Book Issue System
# Library Book Issue System

while True:

    print("\n===== LIBRARY BOOK ISSUE SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Display all books
    if choice == 1:

        file = open("books.txt", "r")
        print(file.read())
        file.close()

    # Search book by ID
    elif choice == 2:

        book_id = input("Enter Book ID: ")

        file = open("books.txt", "r")
        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("Book ID :", data[0])
                print("Book Name :", data[1])
                print("Quantity :", data[2])
                found = True

        if found == False:
            print("Book Not Found")

        file.close()

    # Issue a book
    elif choice == 3:

        book_id = input("Enter Book ID to Issue: ")

        file = open("books.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("books.txt", "w")

        for line in lines:

            data = line.strip().split(",")

            if data[0] == book_id:

                qty = int(data[2])

                if qty > 0:
                    qty = qty - 1
                    print("Book Issued Successfully")
                else:
                    print("Book Not Available")

                line = data[0] + "," + data[1] + "," + str(qty) + "\n"

            file.write(line)

        file.close()

    # Return a book
    elif choice == 4:

        book_id = input("Enter Book ID to Return: ")

        file = open("books.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("books.txt", "w")

        for line in lines:

            data = line.strip().split(",")

            if data[0] == book_id:

                qty = int(data[2]) + 1

                line = data[0] + "," + data[1] + "," + str(qty) + "\n"

                print("Book Returned Successfully")

            file.write(line)

        file.close()

    # Display unavailable books
    elif choice == 5:

        file = open("books.txt", "r")

        print("\nUnavailable Books:")

        for line in file:

            data = line.strip().split(",")

            if int(data[2]) == 0:
                print(data[0], data[1])

        file.close()

    # Display books needing restocking
    elif choice == 6:

        file = open("books.txt", "r")

        print("\nBooks Requiring Restocking:")

        for line in file:

            data = line.strip().split(",")

            if int(data[2]) < 2:
                print(data[0], data[1], data[2])

        file.close()

    # Exit
    elif choice == 7:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")
