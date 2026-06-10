# Warehouse Product Inspection
# Problem Statement
# Product IDs and quality status:
# products = [
# (101, "Pass"),
# (102, "Fail"),
# (103, "Pass"),
# (104, "Fail"),
# (105, "Pass")
# ]
# Write a program to:
# * Display failed product IDs.
# * Count passed and failed products.
# * Calculate pass percentage.
# * Stop checking if 3 failures are found.
# Product IDs and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

# Task 1: Display failed product IDs
print("Failed Product IDs:")

for product in products:
    if product[1] == "Fail":
        print(product[0])

# Task 2: Count passed and failed products
for product in products:
    if product[1] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)

# Task 3: Calculate pass percentage
pass_percentage = (pass_count / len(products)) * 100

print("\nPass Percentage:", pass_percentage)

# Task 4: Stop checking if 3 failures are found
failures = 0

for product in products:
    if product[1] == "Fail":
        failures += 1

    if failures == 3:
        print("3 Failures Found. Stopping Check.")
        break
