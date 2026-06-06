# E-Commerce Order Analysis
# Problem Statement
# An online store records orders as:
# orders = [
# ("Laptop", 55000),
# ("Mouse", 800),
# ("Keyboard", 1500),
# ("Monitor", 12000),
# ("Pen Drive", 600)
# ]
# Write a program to:
# * Display all products costing more than ₹1000.
# * Find the most expensive product.
# * Calculate the total order value.
# * Count products costing below ₹1000.

# Product names and prices
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Task 1: Display all products costing more than ₹1000
print("Products costing more than ₹1000:")

for product in orders:
    if product[1] > 1000:
        print(product[0], product[1])

# Task 2: Find the most expensive product
highest = orders[0]

for product in orders:
    if product[1] > highest[1]:
        highest = product

print("\nMost Expensive Product:")
print(highest[0], highest[1])

# Task 3: Calculate the total order value
total = 0

for product in orders:
    total += product[1]

print("\nTotal Order Value:", total)

# Task 4: Count products costing below ₹1000
count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("\nProducts costing below ₹1000:", count)
