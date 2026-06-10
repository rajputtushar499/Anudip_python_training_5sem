#  Library Book Search
# Problem Statement
# Books available in a library:
# books = [
# ("Python Basics", 5),
# ("Data Science", 0),
# ("Java Programming", 3),
# ("Machine Learning", 0)
# ]
# Write a program to:
# * Display unavailable books.
# * Find all books with more than 2 copies.
# * Count available books.
# * Stop searching once a requested book is found.
# # Book names and available copies
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")

for book in books:
    # Check if copies are 0
    if book[1] == 0:
        print(book[0])

# Find books with more than 2 copies
print("\nBooks with more than 2 copies:")

for book in books:
    # Check if copies are greater than 2
    if book[1] > 2:
        print(book[0], "-", book[1])

# Count available books
count = 0

for book in books:
    # Check if at least 1 copy is available
    if book[1] > 0:
        count += 1

print("\nAvailable Books:", count)

# Search for a book
search_book = "Java Programming"

for book in books:
    # Check if requested book is found
    if book[0] == search_book:
        print("\nBook Found:", book[0])
        break   # Stop searching
