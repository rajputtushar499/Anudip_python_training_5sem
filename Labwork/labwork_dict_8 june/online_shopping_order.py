# Online Shopping Order Analytics
# Problem Statement
# An e-commerce company stores product sales data as:
# sales = { 
# "Laptop": 15, 
# "Mouse": 45, 
# "Keyboard": 32,
# "Monitor": 12, 
# "Headphones": 28, 
# "Printer": 8, 
# "Webcam": 20,
# "Speaker": 18,
# "Tablet": 10,
# "Router": 25 
# }
# Tasks
# 1.Display products sold more than 20 times.
# 2.Find the best-selling product.
# 3. Find the least-selling product.
# 4.Calculate total products sold.
# 5. Create a list of products requiring promotion (sales < 15).
# 6.Count products having sales between 10 and 30.
# Sample Output
# Products Sold More Than 20 Times: 
# Mouse
# Keyboard 
# Headphones
# Router
# Best Selling Product: Mouse (45)
# Least Selling Product: Printer (8)
# Total Units Sold: 213
# Products Requiring Promotion: 
# ['Monitor', 'Printer', 'Tablet']
# Products Having Sales Between 10 and 30: 6

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product in sales:
    if sales[product] > 20:
        print(product)

# 2. Best-selling product
highest = max(sales, key=sales.get)
print("Best Selling Product:", highest, sales[highest])

# 3. Least-selling product
lowest = min(sales, key=sales.get)
print("Least Selling Product:", lowest, sales[lowest])

# 4. Total products sold
total = sum(sales.values())
print("Total Units Sold:", total)

# 5. Products requiring promotion
promotion = []

for product in sales:
    if sales[product] < 15:
        promotion.append(product)

print("Products Requiring Promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0

for product in sales:
    if sales[product] >= 10 and sales[product] <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)
