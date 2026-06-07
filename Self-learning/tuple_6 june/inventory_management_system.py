# Inventory Dictionary
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Products with stock less than 10
print("Products with stock less than 10:")
for item in inventory:
    if inventory[item] < 10:
        print(item, inventory[item])

# Count products with stock more than 50
count = 0

for item in inventory:
    if inventory[item] > 50:
        count += 1

print("\nProducts with stock more than 50:", count)

# Find product with minimum stock
min_product = ""
min_stock = 999

for item in inventory:
    if inventory[item] < min_stock:
        min_stock = inventory[item]
        min_product = item

print("\nProduct with minimum stock:")
print(min_product, min_stock)

# Products that need restocking (stock < 20)
restock = []

for item in inventory:
    if inventory[item] < 20:
        restock.append(item)

print("\nProducts that need restocking:")
print(restock)

# Calculate total inventory count
total = 0

for item in inventory:
    total += inventory[item]

print("\nTotal Inventory Count:", total)
