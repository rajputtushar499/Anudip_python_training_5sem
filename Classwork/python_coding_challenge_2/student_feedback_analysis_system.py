# Student Feedback Analysis System 
# Problem Statement 
# A training institute collects feedback from students after completing a Python course. The feedback 
# comments are stored in a text file named feedback.txt. 
# Sample Input/Data (feedback.txt) 
# The sessions were very interactive and informative. 
# Excellent teaching methodology and practical examples. 
# The pace of the course was appropriate. 
# More real-world projects should be included. 
# The trainer explained concepts very clearly. 
# Tasks 
# 1. Count the total number of lines.  
# 2. Count the total number of words.  
# 3. Count the total number of characters.  
# 4. Find the longest feedback comment.  
# 5. Find the shortest feedback comment.  
# 6. Count the total number of vowels present in the file.  
# Sample Output 
# Total Lines: 5 
 
# Total Words: 35 
 
# Total Characters: 220 
 
# Longest Feedback: 
# Excellent teaching methodology and practical examples. 
 
# Shortest Feedback: 
# The pace of the course was appropriate. 
 
# Total Vowels: 76
#------------------------------------------------------------

# feedback.txt
# The sessions were very interactive and informative.
# Excellent teaching methodology and practical examples.
# The pace of the course was appropriate.
# More real-world projects should be included.
# The trainer explained concepts very clearly.

#-------------------------------------------------------------
# Student Feedback Analysis System

file = open("feedback.txt", "r")

lines = file.readlines()

file.close()

#------------------------------------------------------------
# 1. Count total lines
#------------------------------------------------------------

total_lines = len(lines)

print("Total Lines:", total_lines)

#------------------------------------------------------------
# 2. Count total words
#------------------------------------------------------------

word_count = 0

for line in lines:
    words = line.split()
    word_count = word_count + len(words)

print("\nTotal Words:", word_count)

#----------------------------------------------------------------
# 3. Count total characters
#----------------------------------------------------------------

char_count = 0

for line in lines:
    char_count = char_count + len(line)

print("\nTotal Characters:", char_count)

#-----------------------------------------------------------------
# 4. Find longest feedback
#-----------------------------------------------------------------

longest = lines[0]

for line in lines:
    if len(line) > len(longest):
        longest = line

print("\nLongest Feedback:")
print(longest)

#------------------------------------------------------------------
# 5. Find shortest feedback
#------------------------------------------------------------------

shortest = lines[0]

for line in lines:
    if len(line) < len(shortest):
        shortest = line

print("Shortest Feedback:")
print(shortest)

#------------------------------------------------------------------
# 6. Count vowels
#------------------------------------------------------------------

vowel_count = 0

for line in lines:
    for ch in line:
        if ch.lower() in "aeiou":
            vowel_count = vowel_count + 1

print("Total Vowels:", vowel_count)
