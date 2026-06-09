#  E-Commerce Inventory & Sales Dashboard 
# Problem Statement 
# An online store wants to manage products and sales. 
# Example Structure 
# products = { 
#     "P101": { 
#         "name": "Laptop", 
#         "price": 55000, 
#         "stock": 12, 
#         "sold": 25 
#     } 
# } 
# Maintain records of at least 30 products. 
# Requirements 
# 1. Display all products.  
# 2. Add a new product.  
# 3. Update stock after sales.  
# 4. Find out-of-stock products.  
# 5. Find products with stock less than 5.  
# 6. Calculate total inventory value.  
# 7. Find best-selling product.  
# 8. Find least-selling product.  
# 9. Calculate total revenue generated.  
# 10. Generate a low-stock report.  
# 11. Display products whose sales exceed the average sales.  
# 12. Create a dictionary of products eligible for promotion (sales < 10).  
# Challenge 
# Generate a complete business report.

# E-Commerce Inventory & Sales Dashboard

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 500, "stock": 20, "sold": 50},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 8, "sold": 30},
    "P104": {"name": "Monitor", "price": 15000, "stock": 3, "sold": 15},
    "P105": {"name": "Printer", "price": 8000, "stock": 0, "sold": 12},
    "P106": {"name": "Scanner", "price": 7000, "stock": 2, "sold": 8},
    "P107": {"name": "Speaker", "price": 2500, "stock": 10, "sold": 22},
    "P108": {"name": "Webcam", "price": 1800, "stock": 4, "sold": 9},
    "P109": {"name": "Headphone", "price": 3000, "stock": 6, "sold": 18},
    "P110": {"name": "Tablet", "price": 20000, "stock": 5, "sold": 11}
}

# Task 1: Display all products
print("All Products:")
for pid in products:
    print(pid, products[pid])

# Task 2: Add a new product
pid = input("Enter Product ID: ")
name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
stock = int(input("Enter Stock: "))
sold = int(input("Enter Sold Quantity: "))

products[pid] = {
    "name": name,
    "price": price,
    "stock": stock,
    "sold": sold
}

print("Product Added Successfully")

# Task 3: Update stock after sales
product_id = input("Enter Product ID: ")

if product_id in products:
    qty = int(input("Enter Sold Quantity: "))
    products[product_id]["stock"] -= qty
    products[product_id]["sold"] += qty
    print("Stock Updated")
else:
    print("Product Not Found")

# Task 4: Find out-of-stock products
print("Out of Stock Products:")

for pid in products:
    if products[pid]["stock"] == 0:
        print(pid, products[pid])

# Task 5: Find products with stock less than 5
print("Products with Stock Less Than 5:")

for pid in products:
    if products[pid]["stock"] < 5:
        print(pid, products[pid])

# Task 6: Calculate total inventory value
total_value = 0

for pid in products:
    total_value += products[pid]["price"] * products[pid]["stock"]

print("Total Inventory Value:", total_value)

# Task 7: Find best-selling product
best_product = max(products,key=lambda x: products[x]["sold"])

print("Best Selling Product:")
print(best_product, products[best_product])

# Task 8: Find least-selling product
least_product = min(products,key=lambda x: products[x]["sold"])

print("Least Selling Product:")
print(least_product, products[least_product])

# Task 9: Calculate total revenue generated
revenue = 0

for pid in products:
    revenue += products[pid]["price"] * products[pid]["sold"]

print("Total Revenue:", revenue)

# Task 10: Generate low-stock report
print("Low Stock Report:")

for pid in products:
    if products[pid]["stock"] < 5:
        print(pid, products[pid])

# Task 11: Products whose sales exceed average sales
total_sales = 0

for pid in products:
    total_sales += products[pid]["sold"]

average_sales = total_sales / len(products)

print("Products Above Average Sales:")

for pid in products:
    if products[pid]["sold"] > average_sales:
        print(pid, products[pid])

# Task 12: Products eligible for promotion
promotion = {}

for pid in products:
    if products[pid]["sold"] < 10:
        promotion[pid] = products[pid]

print("Promotion Products:")

for pid in promotion:
    print(pid, promotion[pid])

# Challenge: Business Report
print("===== BUSINESS REPORT =====")
print("Total Products:", len(products))
print("Total Inventory Value:", total_value)
print("Total Revenue:", revenue)
print("Best Selling Product:", best_product)
print("Least Selling Product:", least_product)
print("Products Eligible for Promotion:", len(promotion))
