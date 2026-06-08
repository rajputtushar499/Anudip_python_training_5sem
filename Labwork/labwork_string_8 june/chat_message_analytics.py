# Chat Message Analytics
# Problem Statement
# A chat application stores a message:
# Python is awesome and Python is easy to learn
# Tasks
# Write a program to:
# 1.Count total characters.
# 2.Count total words.
# 3.Find the longest word.
# 4.Find the shortest word.
# 5.Count how many times the word "Python" appears.
# 6.Create a list of words having more than 4 characters.
# 7.Display all words starting with a vowel.
# 8.Count the number of vowels and consonants.
# Sample Output
# Message:
# Python is awesome and Python is easy to learn 
# Total Characters: 45 
# Total Words: 8 
# Longest Word: awesome
# Shortest Word: is 
# Occurrences of Python: 2 
# Words Longer Than 4 Characters:
# ['Python', 'awesome', 'Python', 'learn'] 
# Vowels: 16 
# Consonants: 22

# Chat Message Analytics

message = "Python is awesome and Python is easy to learn"

# Task 1: Count total characters
total_characters = len(message)
print("Total Characters:", total_characters)

# Task 2: Count total words
words = message.split()
total_words = len(words)
print("Total Words:", total_words)

# Task 3: Find the longest word
longest_word = max(words, key=len)
print("Longest Word:", longest_word)

# Task 4: Find the shortest word
shortest_word = min(words, key=len)
print("Shortest Word:", shortest_word)

# Task 5: Count how many times the word 'Python' appears
python_count = words.count("Python")
print("Occurrences of Python:", python_count)

# Task 6: Create a list of words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# Task 7: Display all words starting with a vowel
print("Words Starting With a Vowel:")
for word in words:
    if word[0].lower() in "aeiou":
        print(word)

# Task 8: Count the number of vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
