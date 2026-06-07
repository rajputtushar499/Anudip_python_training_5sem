# Electricity Consumption Report
# Sample Data
# units = { "House101": 320,
# "House102": 180,
# "House103": 450,
# "House104": 290,
# "House105": 150,
# "House106": 510,
# "House107": 220,
# "House108": 390,
# "House109": 170, 
# "House110": 260
# }
# Tasks
# Display houses consuming more than 300 units.
# Count houses consuming less than 200 units.
# Find the house with the highest consumption.
# Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).
# Categorize houses as:
# Low: < 200 units
# Medium: 200–350 units
# High: > 350 units

# Electricity Consumption Report

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# 1. Houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, unit in units.items():
    if unit > 300:
        print(house, ":", unit)

# 2. Count houses consuming less than 200 units
count = 0
for unit in units.values():
    if unit < 200:
        count += 1

print("Number of houses consuming less than 200 units:", count)

# 3. House with highest consumption
highest_house = max(units, key=units.get)
print("House with highest consumption:")
print(highest_house, ":", units[highest_house])

# 4. Houses eligible for energy-saving awareness campaign
campaign_list = []

for house, unit in units.items():
    if unit > 400:
        campaign_list.append(house)

print("Energy-saving awareness campaign list:")
print(campaign_list)

# 5. Categorize houses
print("House Categories:")

for house, unit in units.items():
    if unit < 200:
        category = "Low"
    elif unit <= 350:
        category = "Medium"
    else:
        category = "High"

    print(house, ":", category)
