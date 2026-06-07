# Mobile Contact Directory
# Sample Data
# contacts = { 
# "Amit": "9876543210",
# "Priya": "9876543211", 
# "Rohan": "9876543212",
# "Neha": "9876543213",
# "Anjali": "9876543214", 
# "Karan": "9876543215", 
# "Pooja": "9876543216", 
# "Arjun": "9876543217", 
# "Sneha": "9876543218",
# "Rahul": "9876543219" 
# }
# Tasks
# Display all contact names in alphabetical order.
# Count the total number of contacts.
# Search for a given contact name.
# Create a list of contacts whose names start with a vowel.
# Stop the search using break once the required contact is found.

# Contact Dictionary
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display names in alphabetical order
print("Contacts in Alphabetical Order:")
for name in sorted(contacts):
    print(name)

# Count total contacts
print("Total Contacts:", len(contacts))

# Search a contact
search_name = input("Enter contact name to search: ")

for name in contacts:
    if name == search_name:
        print("Contact Found:", name, contacts[name])
        break
else:
    print("Contact Not Found")

# Contacts starting with vowels
vowel_contacts = []

for name in contacts:
    if name[0] in "AEIOUaeiou":
        vowel_contacts.append(name)

print("Contacts starting with vowels:")
print(vowel_contacts)
