#  Smart Library Management System 
# Problem Statement 
# Create a digital library management system. 
# Example Structure 
# library = { 
#     "B101": { 
#         "title": "Python Basics", 
#         "author": "ABC", 
#         "copies": 5 
#     } 
# } 
# Maintain records of at least 30 books. 
# Requirements 
# 1. Add a book.  
# 2. Remove a book.  
# 3. Search a book by ID.  
# 4. Search by title.  
# 5. Update available copies.  
# 6. Issue a book.  
# 7. Return a book.  
# 8. Display books with fewer than 3 copies.  
# 9. Display books that are unavailable.  
# 10. Find the most available book.  
# 11. Generate a restocking report.  
# 12. Create a separate dictionary of books requiring immediate purchase.  
# Challenge 
# Generate a complete library summary report. 

# Smart Library Management System

library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Science", "author": "XYZ", "copies": 2},
    "B103": {"title": "Machine Learning", "author": "PQR", "copies": 0},
    "B104": {"title": "AI Fundamentals", "author": "LMN", "copies": 8},
    "B105": {"title": "Web Development", "author": "DEF", "copies": 1}
}

# 1. Add a book
library["B106"] = {
    "title": "Cyber Security",
    "author": "GHI",
    "copies": 4
}
print("Book Added Successfully")

# 2. Remove a book
del library["B105"]
print("Book B105 Removed")

# 3. Search a book by ID
book_id = "B101"
print("Search By ID:")
if book_id in library:
    print(library[book_id])

# 4. Search by title
title = "Data Science"
print("Search By Title:")
for bid, details in library.items():
    if details["title"] == title:
        print(bid, details)

# 5. Update available copies
library["B102"]["copies"] = 6
print("Updated Copies of B102:", library["B102"]["copies"])

# 6. Issue a book
if library["B101"]["copies"] > 0:
    library["B101"]["copies"] -= 1
    print("Book Issued Successfully")

# 7. Return a book
library["B101"]["copies"] += 1
print("Book Returned Successfully")

# 8. Display books with fewer than 3 copies
print("Books with Fewer Than 3 Copies:")
for bid, details in library.items():
    if details["copies"] < 3:
        print(bid, details["title"], details["copies"])

# 9. Display books that are unavailable
print("Unavailable Books:")
for bid, details in library.items():
    if details["copies"] == 0:
        print(bid, details["title"])

# 10. Find the most available book
most_available = max(library, key=lambda x: library[x]["copies"])
print("Most Available Book:")
print(most_available, library[most_available]["title"],
      library[most_available]["copies"], "copies")

# 11. Generate a restocking report
print("Restocking Report:")
for bid, details in library.items():
    if details["copies"] < 3:
        print(bid, details["title"], "-", details["copies"], "copies left")

# 12. Create a separate dictionary of books requiring immediate purchase
purchase_books = {}

for bid, details in library.items():
    if details["copies"] <= 1:
        purchase_books[bid] = details

print("Books Requiring Immediate Purchase:")
print(purchase_books)

# Challenge - Complete Library Summary Report
print("Library Summary Report")
print("Total Books:", len(library))

total_copies = 0
for details in library.values():
    total_copies += details["copies"]

print("Total Available Copies:", total_copies)

print("All Books:")
for bid, details in library.items():
    print(bid, "-", details["title"], "-", details["author"],
          "-", details["copies"], "copies")
