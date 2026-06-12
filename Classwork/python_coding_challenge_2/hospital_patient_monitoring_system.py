#  Hospital Patient Monitoring System 
# Problem Statement 
# Patient heart rates are recorded below. 
# Sample Data 
# heart_rate = { 
#     "P101": 72, 
#     "P102": 105, 
#     "P103": 88, 
#     "P104": 120, 
#     "P105": 65, 
#     "P106": 98, 
#     "P107": 110, 
#     "P108": 70, 
#     "P109": 85, 
#     "P110": 130 
# } 
# Tasks 
# 1. Display critical patients (heart rate >100).  
# 2. Find highest and lowest heart rate.  
# 3. Calculate average heart rate.  
# 4. Count stable patients (60–100 bpm).  
# Sample Output 
# Critical Patients: 
# P102 
# P104 
# P107 
# P110 
 
# Highest Heart Rate: 
# P110 (130 bpm) 
 
# Lowest Heart Rate: 
# P105 (65 bpm) 
 
# Average Heart Rate: 94.3 bpm 
 
# Stable Patients: 6

#---------------------------------------------------------
# City Temperature Monitoring System

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

#---------------------------------------------------------
# 1. Cities with temperature above 40°C
#---------------------------------------------------------

print("Cities Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city)

#------------------------------------------------------------
# 2. Hottest City
#------------------------------------------------------------ 

highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("Hottest City:")
print(hottest_city, highest_temp, "°C")

#-----------------------------------------------------------------
# 3. Coolest City
#-----------------------------------------------------------------

lowest_temp = 100

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("Coolest City:")
print(coolest_city, lowest_temp, "°C")

#---------------------------------------------------------
# 4. Average Temperature
#---------------------------------------------------------

total = 0

for city in temperature:
    total = total + temperature[city]

average = total / len(temperature)

print("Average Temperature:", average, "°C")

#---------------------------------------------------------
# 5. Pleasant Cities
#---------------------------------------------------------

pleasant_cities = []

for city in temperature:
    if temperature[city] < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:")
print(pleasant_cities)
