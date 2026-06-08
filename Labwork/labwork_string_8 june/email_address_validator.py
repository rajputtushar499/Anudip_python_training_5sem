# Email Address Validator
# Problem Statement
# A user enters an email address:
# rahul.sharma2026@gmail.com
# Tasks
# Write a program to:
# 1.Extract username.
# 2.Extract domain name.
# 3.Extract extension.
# 4.Count digits present in username.
# 5.Count special characters.
# 6.Check whether:
# oExactly one '@' exists.
# oAt least one '.' exists after '@'.
# 7.Display Valid Email or Invalid Email.
# Sample Output
# Email: rahul.sharma2026@gmail.com
# Username: rahul.sharma2026 
# Domain: gmail 
# Extension: com 
# Digits Found: 4 
# Special Characters Found: 2 
# Email Status: Valid

# Email Address Validator

email = "rahul.sharma2026@gmail.com"

# Task 1: Extract username
username = email.split("@")[0]
print("Username:", username)

# Task 2: Extract domain name
domain = email.split("@")[1].split(".")[0]
print("Domain:", domain)

# Task 3: Extract extension
extension = email.split(".")[-1]
print("Extension:", extension)

# Task 4: Count digits present in username
digits = 0

for ch in username:
    if ch.isdigit():
        digits += 1

print("Digits Found:", digits)

# Task 5: Count special characters
special = 0

for ch in email:
    if not ch.isalnum():
        special += 1

print("Special Characters Found:", special)

# Task 6 & 7: Validate Email

if email.count("@") == 1 and "." in email.split("@")[1]:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")
