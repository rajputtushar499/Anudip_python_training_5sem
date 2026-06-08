# Username Generator System
# Problem Statement
# A student enters:
# Rahul Sharma
# Tasks
# Generate a username using the rules:
# 1.Remove spaces.
# 2.Convert to lowercase.
# 3.Append current year (2026).
# 4.If username length exceeds 12, keep only first 12 characters.
# 5.Count vowels in the generated username.
# 6.Count consonants.
# 7.Display username statistics.
# Sample Output
# Original Name: Rahul Sharma 
# Generated Username: rahulsharma2026
# Username Length: 15 
# Vowels: 5 
# Consonants: 10
# Status: Username Generated Successfully

# Username Generator System

name = "Rahul Sharma"

# Task 1: Remove spaces
username = name.replace(" ", "")
print("After Removing Spaces:", username)

# Task 2: Convert to lowercase
username = username.lower()
print("Lowercase Username:", username)

# Task 3: Append current year
username = username + "2026"
print("Username with Year:", username)

# Task 4: If length exceeds 12, keep only first 12 characters
if len(username) > 12:
    username = username[:12]

print("Generated Username:", username)

# Task 5 & 6: Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Task 7: Display username statistics
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")
