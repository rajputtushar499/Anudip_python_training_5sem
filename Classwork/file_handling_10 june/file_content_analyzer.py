#  File Content Analyzer 
# A publishing company maintains articles in text files and wants to generate basic statistics about the content 
# stored in these files. As a software developer, you have been assigned the task of creating a program that 
# reads the contents of a text file and analyzes the information present in it. 
# Requirements 
# Write a Python program that reads data from a text file and displays the following details: 
# 1. Total number of vowels present in the file.  
# 2. Total number of characters present in the file (including spaces and special characters).  
# 3. Total number of lines present in the file.  
# Sample File Content (article.txt) 
# Python is an easy-to-learn programming language. 
# It supports multiple programming paradigms. 
# File handling allows programs to work with data stored in files. 
# Expected Output 
# File Analysis Report 
 
# Total Number of Vowels    : 42 
# Total Number of Characters: 153 
# Total Number of Lines     : 3

file = open(r"file1.txt", "r")

vowels = 0
characters = 0
lines = 0

for line in file:
    lines += 1

    for ch in line:
        characters += 1

        if ch.lower() in "aeiou":
            vowels += 1

file.close()

print("No. of vowels:", vowels)
print("No. of characters:", characters)
print("No. of lines:", lines)
