# License Key Verification System
# Problem Statement
# A software license key is entered:
# ABCD-EFGH-IJKL-MNOP
# Tasks
# Write a program to:
# 1.Verify there are exactly 4 groups.
# 2.Verify each group contains exactly 4 characters.
# 3.Count total letters.
# 4.Count vowels.
# 5.Remove hyphens and display the merged key.
# 6.Create a list containing all groups.
# 7.Display whether the key format is valid.
# Sample Output
# License Key: ABCD-EFGH-IJKL-MNOP
# Groups: ['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
# Number of Groups: 4 
# Total Letters: 16
# Total Vowels: 4 
# Merged Key: ABCDEFGHIJKLMNOP
# License Key Status: Valid

# License Key Verification System

# License Key Verification System

key = "ABCD-EFGH-IJKL-MNOP"

# Split into groups
groups = key.split("-")

print("Groups:", groups)
print("Number of Groups:", len(groups))

# Count letters
letters = 0
for ch in key:
    if ch.isalpha():
        letters += 1

print("Total Letters:", letters)

# Count vowels
vowels = 0
for ch in key:
    if ch in "AEIOU":
        vowels += 1

print("Total Vowels:", vowels)
# Task 5: Remove hyphens
merged_key = key.replace("-", "")
print("Merged Key:", merged_key)

# Task 7: Validate License Key
valid = True

if len(groups) != 4:
    valid = False

for group in groups:
    if len(group) != 4:
        valid = False

if valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")
