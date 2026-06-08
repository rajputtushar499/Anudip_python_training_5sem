# Password Strength Analyzer
# Problem Statement
# A user enters a password.
# Python@2026!
# Tasks
# Write a program to determine whether the password is Strong, Medium, or Weak.
# Rules:
# •Minimum length 8
# •Contains at least:
# o 1 uppercase letter
# o 1 lowercase letter
# o 1 digit
# o 1 special character
# Additionally:
# 1.Count uppercase letters.
# 2.Count lowercase letters.
# 3.Count digits.
# 4.Count special characters.
# 5.Display all digits separately.
# 6.Display all special characters separately.
# Sample Output
# Password: Python@2026! 
# Uppercase Letters: 1 
# Lowercase Letters: 5 
# Digits: 4 
# Special Characters: 2 
# Digits Found: ['2', '0', '2', '6'] 
# Special Characters Found: ['@', '!'] 
# Password Strength: Strong

password = "Python@2026!"
# 1. Count uppercase letters
uppercase_count = 0
for char in password:
    if char.isupper():
        uppercase_count += 1
print("Uppercase Letters:", uppercase_count)

# 2. Count lowercase letters
lowercase_count = 0
for char in password:
    if char.islower():
        lowercase_count += 1
print("Lowercase Letters:", lowercase_count)

# 3. Count digits
digit_count = 0
for char in password:
    if char.isdigit():
        digit_count += 1
print("Digits:", digit_count)

# 4. Count special characters
special_count = 0
for char in password:
    if not char.isalnum():
        special_count += 1
print("Special Characters:", special_count)

# 5. Display all digits separately
digits_found = []
for char in password:
    if char.isdigit():
        digits_found.append(char)
print("Digits Found:", digits_found)

# 6. Display all special characters separately
special_chars_found = []
for char in password:
    if not char.isalnum():
        special_chars_found.append(char)
print("Special Characters Found:", special_chars_found)

# Determine password strength
if len(password) >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1:
    print("Password Strength: Strong")
elif len(password) >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
