# Employee ID Validation and Analysis System
# Problem Statement
# A company generates employee IDs in the following format:
# EMP2026ANUJ458
# Tasks
# Write a program to:
# 1.Count the number of uppercase letters.
# 2.Count the number of digits.
# 3.Extract the joining year.
# 4.Extract the employee name.
# 5.Check whether the ID follows these rules:
# o Starts with "EMP"
# o Contains exactly 4 digits for the year
# o Ends with exactly 3 digits
# 6.Create a list containing all digits present in the ID.
# 7.Find the sum of all digits present in the ID.
# 8.Display whether the ID is valid or invalid.
# Sample Output
# Employee ID: EMP2026ANUJ458
# Uppercase Letters: 7 
# Digits: 7 
# Joining Year: 2026 
# Employee Name: ANUJ 
# Digit List: [2, 0, 2, 6, 4, 5, 8] 
# Sum of Digits: 27
# ID Status: Valid

employee_id = "EMP2026ANUJ458"
# 1. Count the number of uppercase letters  
uppercase_count=0
for char in employee_id:
    if char.isupper():
        uppercase_count += 1
print("Uppercase Letters:", uppercase_count)

# 2. Count the number of digits
digit_count=0
for char in employee_id:
    if char.isdigit():
        digit_count += 1    
print("Digits:", digit_count)

# 3. Extract the joining year
joining_year = employee_id[3:7]
print("Joining Year:", joining_year)

# 4. Extract the employee name
employee_name = employee_id[7:11]
print("Employee Name:", employee_name)

# 5. Check whether the ID follows the rules
starts_emp = employee_id.startswith("EMP")
year_valid = employee_id[3:7].isdigit()
end_digits = employee_id[-3:]
end_valid = end_digits.isdigit()
if starts_emp and year_valid and end_valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
    
# 6. Create a list containing all digits present in the ID
digit_list = [] 
for char in employee_id:
    if char.isdigit():
        digit_list.append(int(char))
print("Digit List:", digit_list)

# 7. Find the sum of all digits present in the ID
digit_sum = sum(digit_list)
print("Sum of Digits:", digit_sum)
