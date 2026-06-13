#  Smart Agriculture Crop Monitoring System 
# Problem Statement 
# Crop moisture levels (%) are stored as follows: 
# moisture = { 
#     "Field1": 55, 
#     "Field2": 30, 
#     "Field3": 72, 
#     "Field4": 28, 
#     "Field5": 64, 
#     "Field6": 35, 
#     "Field7": 80, 
#     "Field8": 42, 
#     "Field9": 25, 
#     "Field10": 68 
# } 
# Tasks 
# 1. Identify fields requiring irrigation (< 40%).  
# 2. Classify fields into Low, Moderate, and High moisture categories.  
# 3. Count fields in each category.  
# 4. Find fields with the highest and lowest moisture levels.  
# 5. Generate an irrigation priority list.  
# Sample Output 
# Fields Requiring Irrigation: 
# Field2 
# Field4 
# Field6 
# Field9 
 
# Low Moisture Fields: 
# ['Field2', 'Field4', 'Field6', 'Field9'] 
 
# Moderate Moisture Fields: 
# ['Field1', 'Field5', 'Field8'] 
 
# High Moisture Fields: 
# ['Field3', 'Field7', 'Field10'] 
 
# Field with Highest Moisture: 
# Field7 (80%) 
 
# Field with Lowest Moisture: 
# Field9 (25%) 
 
# Irrigation Priority List: 
# ['Field9', 'Field4', 'Field2', 'Field6']

#--------------------------------------------------
# Task 1: Identify Fields Requiring Irrigation (< 40%)
#--------------------------------------------------

moisture = {
    "Field1": 55,
    "Field2": 30,
    "Field3": 72,
    "Field4": 28,
    "Field5": 64,
    "Field6": 35,
    "Field7": 80,
    "Field8": 42,
    "Field9": 25,
    "Field10": 68
}

print("Fields Requiring Irrigation:")

for field, level in moisture.items():
    if level < 40:
        print(field)


#--------------------------------------------------
# Task 2: Classify Fields into Low, Moderate, and High
#--------------------------------------------------

low = []
moderate = []
high = []

for field, level in moisture.items():

    if level < 40:
        low.append(field)

    elif level <= 65:
        moderate.append(field)

    else:
        high.append(field)

print("\nLow Moisture Fields:")
print(low)

print("\nModerate Moisture Fields:")
print(moderate)

print("\nHigh Moisture Fields:")
print(high)


#--------------------------------------------------
# Task 3: Count Fields in Each Category
#--------------------------------------------------

print("\nCount of Low Moisture Fields:", len(low))
print("Count of Moderate Moisture Fields:", len(moderate))
print("Count of High Moisture Fields:", len(high))


#--------------------------------------------------
# Task 4: Find Fields with Highest and Lowest Moisture
#--------------------------------------------------

highest_field = max(moisture, key=moisture.get)
lowest_field = min(moisture, key=moisture.get)

print("\nField with Highest Moisture:")
print(highest_field, "(", moisture[highest_field], "%)", sep="")

print("\nField with Lowest Moisture:")
print(lowest_field, "(", moisture[lowest_field], "%)", sep="")


#--------------------------------------------------
# Task 5: Generate Irrigation Priority List
#--------------------------------------------------

priority_list = sorted(low, key=lambda field: moisture[field])

print("\nIrrigation Priority List:")
print(priority_list)
