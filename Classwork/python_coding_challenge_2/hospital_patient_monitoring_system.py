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
# Patient heart rate data
heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Display critical patients (heart rate > 100)
print("Critical Patients:")
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient)

# 2. Find highest and lowest heart rate
highest_patient = max(heart_rate, key=heart_rate.get)
lowest_patient = min(heart_rate, key=heart_rate.get)

print("\nHighest Heart Rate:")
print(f"{highest_patient} ({heart_rate[highest_patient]} bpm)")

print("\nLowest Heart Rate:")
print(f"{lowest_patient} ({heart_rate[lowest_patient]} bpm)")

# 3. Calculate average heart rate
average = sum(heart_rate.values()) / len(heart_rate)

print("\nAverage Heart Rate:")
print(f"{average:.1f} bpm")

# 4. Count stable patients (60–100 bpm)
stable_count = 0

for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable_count += 1

print("\nStable Patients:", stable_count)
