#  Function-Based Temperature Converter 
# Problem Statement 
# Daily temperatures recorded in Celsius are given below. 
# Sample Data 
# temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
# Tasks 
# Create functions to: 
# 1. Convert Celsius to Fahrenheit.  
# 2. Display all temperatures in Fahrenheit.  
# 3. Find the highest Fahrenheit temperature.  
# 4. Find the lowest Fahrenheit temperature.  
# 5. Calculate the average Fahrenheit temperature.  
# Sample Output 
# Temperatures in Fahrenheit: 
# 77.0 
# 86.0 
# 95.0 
# 104.0 
# 82.4 
# 89.6 
# 100.4 
# 71.6 
# 80.6 
# 87.8 
# Highest Temperature: 104.0°F 
# Lowest Temperature: 71.6°F 
# A company wants to maintain backups of important documents. Create a program to copy the contents of 
# one file into another. 
# Average Temperature: 87.14°F

#--------------------------------------------------
# Task 1: Convert Celsius to Fahrenheit
#--------------------------------------------------

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#--------------------------------------------------
# Task 2: Display all Temperatures in Fahrenheit
#--------------------------------------------------

temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

def display_temperatures():
    print("Temperatures in Fahrenheit:")
    for temp in temperatures:
        print(celsius_to_fahrenheit(temp))


#--------------------------------------------------
# Task 3: Find Highest Fahrenheit Temperature
#--------------------------------------------------

def highest_temperature():
    fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures]
    print("Highest Temperature:", max(fahrenheit), "°F")


#--------------------------------------------------
# Task 4: Find Lowest Fahrenheit Temperature
#--------------------------------------------------

def lowest_temperature():
    fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures]
    print("Lowest Temperature:", min(fahrenheit), "°F")


#--------------------------------------------------
# Task 5: Calculate Average Fahrenheit Temperature
#--------------------------------------------------

def average_temperature():
    fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures]
    average = sum(fahrenheit) / len(fahrenheit)
    print("Average Temperature:", round(average, 2), "°F")


#--------------------------------------------------
# Function Calls
#--------------------------------------------------

display_temperatures()
highest_temperature()
lowest_temperature()
average_temperature()
