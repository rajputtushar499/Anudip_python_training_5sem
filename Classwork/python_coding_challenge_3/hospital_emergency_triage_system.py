#  Hospital Emergency Triage System 
# Problem Statement 
# Patients arriving at the emergency ward are categorized as: 
# patients = [ 
#     ("P101", "Critical"), 
#     ("P102", "Stable"), 
#     ("P103", "Critical"), 
#     ("P104", "Moderate"), 
#     ("P105", "Stable"), 
#     ("P106", "Critical"), 
#     ("P107", "Moderate"), 
#     ("P108", "Stable"), 
#     ("P109", "Critical"), 
#     ("P110", "Moderate") 
# ] 
# Tasks 
# 1. Count patients in each category.  
# 2. Display IDs of critical patients.  
# 3. Create separate lists for Critical, Moderate, and Stable patients.  
# 4. Determine which category requires maximum attention.  
# 5. Save critical patient IDs to critical_patients.txt.  
# Sample Output 
# Patient Count by Category: 
# Critical : 4 
# Moderate : 3 
# Stable : 3 
 
# Critical Patients: 
# P101 
# P103 
# P106 
# P109 
 
# Critical Patients List: 
# ['P101', 'P103', 'P106', 'P109'] 
 
# Moderate Patients List: 
# ['P104', 'P107', 'P110'] 
 
# Stable Patients List: 
# ['P102', 'P105', 'P108'] 
 
# Category Requiring Maximum Attention: 
# Critical 
 
# Critical Patient Report Generated Successfully.

#--------------------------------------------------
# Task 1: Count Patients in Each Category
#--------------------------------------------------

patients = [
    ("P101", "Critical"),
    ("P102", "Stable"),
    ("P103", "Critical"),
    ("P104", "Moderate"),
    ("P105", "Stable"),
    ("P106", "Critical"),
    ("P107", "Moderate"),
    ("P108", "Stable"),
    ("P109", "Critical"),
    ("P110", "Moderate")
]

critical_count = 0
moderate_count = 0
stable_count = 0

for patient_id, category in patients:

    if category == "Critical":
        critical_count += 1

    elif category == "Moderate":
        moderate_count += 1

    elif category == "Stable":
        stable_count += 1

print("Patient Count by Category:")
print("Critical :", critical_count)
print("Moderate :", moderate_count)
print("Stable :", stable_count)


#--------------------------------------------------
# Task 2: Display IDs of Critical Patients
#--------------------------------------------------

print("\nCritical Patients:")

for patient_id, category in patients:
    if category == "Critical":
        print(patient_id)


#--------------------------------------------------
# Task 3: Create Separate Lists for Categories
#--------------------------------------------------

critical_patients = []
moderate_patients = []
stable_patients = []

for patient_id, category in patients:

    if category == "Critical":
        critical_patients.append(patient_id)

    elif category == "Moderate":
        moderate_patients.append(patient_id)

    elif category == "Stable":
        stable_patients.append(patient_id)

print("\nCritical Patients List:")
print(critical_patients)

print("\nModerate Patients List:")
print(moderate_patients)

print("\nStable Patients List:")
print(stable_patients)


#--------------------------------------------------
# Task 4: Determine Category Requiring Maximum Attention
#--------------------------------------------------

if critical_count >= moderate_count and critical_count >= stable_count:
    attention_category = "Critical"

elif moderate_count >= stable_count:
    attention_category = "Moderate"

else:
    attention_category = "Stable"

print("\nCategory Requiring Maximum Attention:")
print(attention_category)


#--------------------------------------------------
# Task 5: Save Critical Patient IDs to File
#--------------------------------------------------

file = open("critical_patients.txt", "w")

for patient_id in critical_patients:
    file.write(patient_id + "\n")

file.close()

print("\nCritical Patient Report Generated Successfully.")
