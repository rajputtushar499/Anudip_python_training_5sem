# : Space Mission Telemetry Analyzer 
# Problem Statement 
# Sensor readings are stored in telemetry.txt. 
# 101 
# 98 
# 105 
# 110 
# 112 
# 95 
# 90 
# 88 
# 120 
# 102 
# Tasks 
# 1. Read all sensor readings.  
# 2. Display abnormal readings (< 90 or > 110).  
# 3. Calculate average sensor value.  
# 4. Count normal and abnormal readings.  
# 5. Store abnormal readings in alerts.txt.  
# Sample Output 
# Abnormal Sensor Readings: 
# 88 
# 120 
 
# Average Sensor Value: 
# 102.1 
 
# Normal Readings: 8 
# Abnormal Readings: 2 
 
# Alert File Generated Successfully.

#--------------------------------------------------
# Task 1: Read All Sensor Readings
#--------------------------------------------------

file = open("telemetry.txt", "r")
readings = file.readlines()
file.close()

sensor_values = []

for reading in readings:
    sensor_values.append(int(reading.strip()))


#--------------------------------------------------
# Task 2: Display Abnormal Readings (< 90 or > 110)
#--------------------------------------------------

abnormal_readings = []

print("Abnormal Sensor Readings:")

for value in sensor_values:
    if value < 90 or value > 110:
        abnormal_readings.append(value)
        print(value)


#--------------------------------------------------
# Task 3: Calculate Average Sensor Value
#--------------------------------------------------

average = sum(sensor_values) / len(sensor_values)

print("\nAverage Sensor Value:")
print(round(average, 1))


#--------------------------------------------------
# Task 4: Count Normal and Abnormal Readings
#--------------------------------------------------

normal_count = 0
abnormal_count = 0

for value in sensor_values:
    if value < 90 or value > 110:
        abnormal_count += 1
    else:
        normal_count += 1

print("\nNormal Readings:", normal_count)
print("Abnormal Readings:", abnormal_count)


#--------------------------------------------------
# Task 5: Store Abnormal Readings in alerts.txt
#--------------------------------------------------

file = open("alerts.txt", "w")

for value in abnormal_readings:
    file.write(str(value) + "\n")

file.close()

print("\nAlert File Generated Successfully.")
