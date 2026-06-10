#  Food Delivery Performance Tracker 
# Problem Statement 
# Delivery times (in minutes) for different orders are given below: 
# delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
# Requirements 
# Create the following functions: 
# 1. fastest_delivery(times) 
# Returns the shortest delivery time. 
# 2. delayed_orders(times) 
# Returns a list of orders taking more than 45 minutes. 
# 3. average_delivery_time(times) 
# Returns the average delivery time. 
# 4. delivery_category(times) 
# Displays order categories: 
# • Fast → ≤ 30 minutes  
# • Normal → 31–45 minutes  
# • Delayed → > 45 minutes  
# Sample Output 
# Fastest Delivery: 18 minutes 
 
# Delayed Orders: 
# [60, 80, 55] 
 
# Average Delivery Time: 
# 40.8 minutes 
 
# Categories: 
# 28 -> Fast 
# 45 -> Normal 
# 60 -> Delayed 
# ...

# Delivery times in minutes
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# ---------------- TASK 1 ----------------
# Find fastest delivery time
def fastest_delivery(times):
    print("Fastest Delivery:", min(times), "minutes")

# ---------------- TASK 2 ----------------
# Find delayed orders (> 45 minutes)
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    print("Delayed Orders:")
    print(delayed)

# ---------------- TASK 3 ----------------
# Calculate average delivery time
def average_delivery_time(times):
    avg = sum(times) / len(times)
    print("Average Delivery Time:", avg, "minutes")

# ---------------- TASK 4 ----------------
# Categorize deliveries
def delivery_category(times):
    print("Categories:")
    for t in times:
        if t <= 30:
            print(t, "-> Fast")
        elif t <= 45:
            print(t, "-> Normal")
        else:
            print(t, "-> Delayed")

# ---------------- MAIN PROGRAM ----------------
fastest_delivery(delivery_time)
print()

delayed_orders(delivery_time)
print()

average_delivery_time(delivery_time)
print()

delivery_category(delivery_time)
