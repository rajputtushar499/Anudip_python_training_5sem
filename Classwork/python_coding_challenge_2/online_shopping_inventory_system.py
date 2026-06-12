#  Online Shopping Inventory System 
# Problem Statement 
# An online store maintains stock quantities of products. 
# Sample Data 
# inventory = { 
#     "Laptop": 15, 
#     "Mouse": 45, 
#     "Keyboard": 32, 
#     "Monitor": 12, 
#     "Headphones": 28, 
#     "Printer": 8, 
#     "Webcam": 20, 
#     "Speaker": 18, 
#     "Tablet": 10, 
#     "Router": 25 
# } 
# Tasks 
# 1. Display products with stock below 15 units.  
# 2. Find the product with maximum stock.  
# 3. Find the product with minimum stock.  
# 4. Calculate total stock available.  
# 5. Create a list of products requiring restocking (<10 units).  
# Sample Output 
# Products with Stock Below 15: 
# Monitor 
# Printer 
# Tablet 
 
# Highest Stock Product: 
# Mouse (45 units) 
 
# Lowest Stock Product: 
# Printer (8 units) 
 
# Total Stock Available: 213 
 
# Products Requiring Restocking: 
# ['Printer']

#---------------------------------------------------------

# Online Shopping Inventory System

inventory = {
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
#---------------------------------------------------------
# 1. Products with stock below 15
#---------------------------------------------------------

print("Products with Stock Below 15:")

for product in inventory:
    if inventory[product] < 15:
        print(product)

#---------------------------------------------------------
# 2. Product with maximum stock
#---------------------------------------------------------

max_stock = 0

for product in inventory:
    if inventory[product] > max_stock:
        max_stock = inventory[product]
        max_product = product

print("Highest Stock Product:")
print(max_product, max_stock, "units")

#---------------------------------------------------------
# 3. Product with minimum stock
#---------------------------------------------------------

min_stock = 1000

for product in inventory:
    if inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product

print("Lowest Stock Product:")
print(min_product, min_stock, "units")

# 4. Calculate total stock
total_stock = 0

for product in inventory:
    total_stock = total_stock + inventory[product]

print("Total Stock Available:", total_stock)

#---------------------------------------------------------
# 5. Products requiring restocking
#---------------------------------------------------------

restock = []

for product in inventory:
    if inventory[product] < 10:
        restock.append(product)

print("Products Requiring Restocking:")
print(restock)
