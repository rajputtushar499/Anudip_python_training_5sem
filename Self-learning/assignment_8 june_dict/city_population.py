# City Population & Development Dashboard 
# Problem Statement 
# The government wants to analyze city data. 
# Store details of at least 30 cities. 
# Example Structure 
# cities = { 
#     "Delhi": { 
#         "population": 32000000, 
#         "area": 1484, 
#         "literacy": 89 
#     } 
# } 
# Requirements 
# 1. Display all city details.  
# 2. Find the most populated city.  
# 3. Find the least populated city.  
# 4. Calculate average population.  
# 5. Display cities with literacy rate above 90%.  
# 6. Display cities with literacy below average.  
# 7. Calculate population density.  
# 8. Find city with highest density.  
# 9. Categorize cities:  
# o Small  
# o Medium  
# o Large  
# 10. Create a development-priority list.  
# 11. Generate separate dictionaries for:  
# o High Literacy Cities  
# o Low Literacy Cities  
# 12. Generate a national summary report.  
# Challenge 
# Rank all cities based on population density.

# City Population & Development Dashboard

cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Bangalore": {"population": 13000000, "area": 709, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 87},
    "Hyderabad": {"population": 10000000, "area": 650, "literacy": 83},
    "Pune": {"population": 7500000, "area": 516, "literacy": 92},
    "Jaipur": {"population": 4000000, "area": 485, "literacy": 84},
    "Lucknow": {"population": 3500000, "area": 631, "literacy": 81},
    "Kanpur": {"population": 3200000, "area": 403, "literacy": 79},
    "Nagpur": {"population": 2900000, "area": 218, "literacy": 91},
    "Indore": {"population": 3200000, "area": 530, "literacy": 87},
    "Bhopal": {"population": 2500000, "area": 463, "literacy": 85},
    "Patna": {"population": 2600000, "area": 250, "literacy": 82},
    "Surat": {"population": 7000000, "area": 461, "literacy": 89},
    "Vadodara": {"population": 2200000, "area": 235, "literacy": 90},
    "Agra": {"population": 1800000, "area": 188, "literacy": 78},
    "Nashik": {"population": 2000000, "area": 267, "literacy": 89},
    "Ranchi": {"population": 1500000, "area": 175, "literacy": 86},
    "Amritsar": {"population": 1200000, "area": 139, "literacy": 88},
    "Meerut": {"population": 1700000, "area": 141, "literacy": 76},
    "Jodhpur": {"population": 1300000, "area": 233, "literacy": 80},
    "Raipur": {"population": 1400000, "area": 226, "literacy": 87},
    "Gwalior": {"population": 1100000, "area": 289, "literacy": 83},
    "Coimbatore": {"population": 1600000, "area": 246, "literacy": 93},
    "Mysore": {"population": 1000000, "area": 156, "literacy": 91},
    "Udaipur": {"population": 700000, "area": 64, "literacy": 89},
    "Shimla": {"population": 200000, "area": 35, "literacy": 94},
    "Panaji": {"population": 120000, "area": 36, "literacy": 95},
    "Gangtok": {"population": 100000, "area": 19, "literacy": 92}
}

# 1. Display all city details
print("All City Details:")
for city, data in cities.items():
    print(city, data)

# 2. Find the most populated city
most_populated = max(cities, key=lambda x: cities[x]["population"])
print("Most Populated City:")
print(most_populated, cities[most_populated]["population"])

# 3. Find the least populated city
least_populated = min(cities, key=lambda x: cities[x]["population"])
print("Least Populated City:")
print(least_populated, cities[least_populated]["population"])

# 4. Calculate average population
total_population = 0
for city in cities:
    total_population += cities[city]["population"]

avg_population = total_population / len(cities)

print("Average Population:")
print(avg_population)

# 5. Display cities with literacy rate above 90%
print("Cities with Literacy Above 90%:")
for city in cities:
    if cities[city]["literacy"] > 90:
        print(city)

# 6. Display cities with literacy below average
total_literacy = 0
for city in cities:
    total_literacy += cities[city]["literacy"]

avg_literacy = total_literacy / len(cities)

print("Cities with Literacy Below Average:")
for city in cities:
    if cities[city]["literacy"] < avg_literacy:
        print(city)

# 7. Calculate population density
print("Population Density:")
for city in cities:
    density = cities[city]["population"] / cities[city]["area"]
    print(city, round(density, 2))

# 8. Find city with highest density
highest_density_city = max(
    cities,
    key=lambda x: cities[x]["population"] / cities[x]["area"]
)

print("City with Highest Density:")
print(highest_density_city)

# 9. Categorize cities
print("City Categories:")
for city in cities:
    pop = cities[city]["population"]

    if pop < 1000000:
        category = "Small"
    elif pop < 5000000:
        category = "Medium"
    else:
        category = "Large"

    print(city, ":", category)

# 10. Create development-priority list
print("Development Priority Cities:")
for city in cities:
    if cities[city]["literacy"] < 85:
        print(city)

# 11. Generate separate dictionaries
high_literacy = {}
low_literacy = {}

for city in cities:
    if cities[city]["literacy"] >= 90:
        high_literacy[city] = cities[city]
    else:
        low_literacy[city] = cities[city]

print("High Literacy Cities:")
print(high_literacy)

print("Low Literacy Cities:")
print(low_literacy)

# 12. Generate national summary report
print("National Summary Report")
print("Total Cities =", len(cities))
print("Average Population =", avg_population)
print("Average Literacy =", round(avg_literacy, 2))

# Challenge: Rank all cities based on population density
density_rank = {}

for city in cities:
    density_rank[city] = cities[city]["population"] / cities[city]["area"]

sorted_density = sorted(
    density_rank.items(),
    key=lambda x: x[1],
    reverse=True
)
