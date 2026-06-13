# : Disaster Relief Resource Allocation 
# Problem Statement 
# Relief materials available at different warehouses are stored as dictionaries. 
#     "Warehouse2": ["Water", "Food", "Tents"], 
#     "Warehouse3": ["Medicine", "Tents", "Clothes"], 
#     "Warehouse4": ["Food", "Water", "Medicine"] 
# } 
# Tasks 
# 1. Display all unique relief items.  
# 2. Find warehouses containing medicines.  
# 3. Count how many warehouses stock each resource.  
# 4. Identify the most widely available resource.  
# 5. Display resources available in all warehouses.  
# Sample Output 
# Unique Resources: 
# {'Food', 'Medicine', 'Blankets', 'Water', 'Tents', 'Clothes'} 
 
# Warehouses with Medicines: 
# Warehouse1 
# Warehouse3 
# Warehouse4 
 
# Resource Availability: 
# Food : 3 
# Medicine : 3 
# Blankets : 1 
# Water : 2 
# Tents : 2 
# Clothes : 1 
 
# Most Widely Available Resources: 
# Food 
# Medicine 
 
# Resources Available in All Warehouses: 
# None

#--------------------------------------------------
# Task 1: Display All Unique Relief Items
#--------------------------------------------------

resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

unique_resources = set()

for items in resources.values():
    unique_resources.update(items)

print("Unique Resources:")
print(unique_resources)


#--------------------------------------------------
# Task 2: Find Warehouses Containing Medicines
#--------------------------------------------------

print("\nWarehouses with Medicines:")

for warehouse, items in resources.items():
    if "Medicine" in items:
        print(warehouse)


#--------------------------------------------------
# Task 3: Count How Many Warehouses Stock Each Resource
#--------------------------------------------------

resource_count = {}

for items in resources.values():
    for item in items:
        if item in resource_count:
            resource_count[item] += 1
        else:
            resource_count[item] = 1

print("\nResource Availability:")

for resource, count in resource_count.items():
    print(resource, ":", count)


#--------------------------------------------------
# Task 4: Identify the Most Widely Available Resource
#--------------------------------------------------

max_count = max(resource_count.values())

print("\nMost Widely Available Resources:")

for resource, count in resource_count.items():
    if count == max_count:
        print(resource)


#--------------------------------------------------
# Task 5: Display Resources Available in All Warehouses
#--------------------------------------------------

common_resources = set(resources["Warehouse1"])

for items in resources.values():
    common_resources = common_resources.intersection(set(items))

print("\nResources Available in All Warehouses:")

if len(common_resources) == 0:
    print("None")
else:
    print(common_resources)
