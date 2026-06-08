# Smart Electricity Billing System 
# Problem Statement 
# Monthly electricity consumption (units) is stored as: 
# units = { 
#     "House101": 320, 
#     "House102": 180, 
#     "House103": 510, 
#     "House104": 275, 
#     "House105": 150, 
#     "House106": 430, 
#     "House107": 220, 
#     "House108": 390, 
#     "House109": 145, 
#     "House110": 600 
# } 
# Tasks 
# 1. Display houses consuming more than 400 units.  
# 2. Find the highest-consuming house.  
# 3. Find the lowest-consuming house.  
# 4. Calculate total units consumed.  
# 5. Create lists:  
# o Low Consumption (< 200)  
# o Medium Consumption (200–400)  
# o High Consumption (> 400)  
# 6. Count houses eligible for an energy-saving campaign (consumption > 300).  
# Sample Output 
# Houses Consuming More Than 400 Units: 
# House103 
# House106 
# House110 
 
# Highest Consumption: 
# House110 (600 units) 
 
# Lowest Consumption: 
# House109 (145 units) 
 
# Total Units Consumed: 3220 
 
# Low Consumption: 
# ['House102', 'House105', 'House109'] 
 
# Medium Consumption: 
# ['House101', 'House104', 'House107', 'House108'] 
 
# High Consumption: 
# ['House103', 'House106', 'House110'] 
 
# Eligible for Energy-Saving Campaign: 5

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house in units:
    if units[house] > 400:
        print(house)

# 2. Highest-consuming house
highest = max(units, key=units.get)
print("Highest Consumption:")
print(highest, units[highest], "units")

# 3. Lowest-consuming house
lowest = min(units, key=units.get)
print("Lowest Consumption:")
print(lowest, units[lowest], "units")

# 4. Total units consumed
total = sum(units.values())
print("Total Units Consumed:", total)

# 5. Create lists
low = []
medium = []
high = []

for house in units:
    if units[house] < 200:
        low.append(house)
    elif units[house] <= 400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption:")
print(low)

print("Medium Consumption:")
print(medium)

print("High Consumption:")
print(high)

# 6. Count houses eligible for energy-saving campaign
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("Eligible for Energy-Saving Campaign:", count)
