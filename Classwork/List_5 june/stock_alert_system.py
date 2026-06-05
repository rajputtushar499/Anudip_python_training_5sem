# List containing stock quantities of products
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# List to store out-of-stock products
out_of_stock = []

# List to store products that need restocking
restock = []

# Variable to count available products
available_count = 0

# List to store products with stock >= 15
good_stock = []

# Loop through each stock quantity
for quantity in stock:

    # Check if product is out of stock
    if quantity == 0:
        out_of_stock.append(quantity)

    # Check if stock is less than 10 (needs restocking)
    elif quantity < 10:
        restock.append(quantity)
        available_count += 1

    # Product is available
    else:
        available_count += 1

    # Add products having stock greater than or equal to 15
    if quantity >= 15:
        good_stock.append(quantity)

# Display out-of-stock products
print("Out of Stock Products:", out_of_stock)

# Display products that need restocking
print("Products Needing Restock:", restock)

# Display total available products
print("Available Products Count:", available_count)

# Display products with stock >= 15
print("Stock >= 15:", good_stock)
