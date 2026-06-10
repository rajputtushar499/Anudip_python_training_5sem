#  Mobile Contact Directory System 
# Problem Statement 
# Contacts are stored in contacts.txt. 
# File Format 
# Anuj,9876543210 
# Rahul,9876543211 
# Priya,9876543212 
# Neha,9876543213 
# Amit,9876543214 
# Sneha,9876543215 
# Karan,9876543216 
# Pooja,9876543217 
# Rohit,9876543218 
# Anjali,9876543219 
# Requirements 
# Create a menu-driven application to: 
# 1. Display all contacts.  
# 2. Search a contact by name.  
# 3. Add a new contact.  
# 4. Update an existing contact number.  
# 5. Delete a contact.  
# 6. Display contacts whose names start with a vowel.  
# 7. Save all modifications back to the file.  

# TASK 1
# Load contacts from file

contacts = {}

try:
    file = open("contacts.txt", "r")

    for line in file:
        name, number = line.strip().split(",")
        contacts[name] = number

    file.close()

except FileNotFoundError:
    print("File not found")


while True:

    print("\n===== MOBILE CONTACT DIRECTORY =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Save Changes")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    # TASK 2
    # Display all contacts
    if choice == 1:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, "-", number)

    # TASK 3
    # Search contact by name
    elif choice == 2:
        search_name = input("Enter name to search: ")

        if search_name in contacts:
            print("Mobile Number:", contacts[search_name])
        else:
            print("Contact not found")

    # TASK 4
    # Add new contact
    elif choice == 3:
        name = input("Enter name: ")
        number = input("Enter mobile number: ")

        contacts[name] = number
        print("Contact added successfully")

    # TASK 5
    # Update existing contact number
    elif choice == 4:
        name = input("Enter contact name: ")

        if name in contacts:
            new_number = input("Enter new mobile number: ")
            contacts[name] = new_number
            print("Contact updated successfully")
        else:
            print("Contact not found")

    # TASK 6
    # Delete contact
    elif choice == 5:
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    # TASK 7
    # Display contacts whose names start with a vowel
    elif choice == 6:
        print("\nContacts Starting With Vowel:")

        for name, number in contacts.items():
            if name[0].lower() in "aeiou":
                print(name, "-", number)

    # TASK 8
    # Save all modifications back to file
    elif choice == 7:
        file = open("contacts.txt", "w")

        for name, number in contacts.items():
            file.write(name + "," + number + "\n")

        file.close()
        print("Changes saved successfully")

    # TASK 9
    # Exit program
    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
