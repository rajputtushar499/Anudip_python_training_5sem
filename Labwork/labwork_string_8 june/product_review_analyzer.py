# Product Review Analyzer
# Problem Statement
# A customer submits a review:
# This product is excellent excellent excellent and very useful
# Tasks
# Write a program to:
# 1.Count total words.
# 2.Create a dictionary containing word frequencies.
# 3.Find the most frequently used word.
# 4.Find all words appearing only once.
# 5.Count words having more than 5 characters.
# 6.Display words in reverse order.
# 7.Create a list of unique words.
# Sample Output
# Total Words: 8
# Word Frequencies: 
# This -> 1 
# product -> 1 
# is -> 1 
# excellent -> 3 
# and -> 1 
# very -> 1 
# useful -> 1 
# Most Frequent Word: excellent 
# Words Appearing Once:
# ['This', 'product', 'is', 'and', 'very', 'useful']
# Unique Words:
# ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']

# Product Review Analyzer

review = "This product is excellent excellent excellent and very useful"

# Task 1: Count total words
words = review.split()
print("Total Words:", len(words))

# Task 2: Create a dictionary containing word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:")
for word in frequency:
    print(word, "->", frequency[word])

# Task 3: Find the most frequently used word
most_frequent = max(frequency, key=frequency.get)
print("Most Frequent Word:", most_frequent)

# Task 4: Find all words appearing only once
once_words = []

for word in frequency:
    if frequency[word] == 1:
        once_words.append(word)

print("Words Appearing Once:", once_words)

# Task 5: Count words having more than 5 characters
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words Having More Than 5 Characters:", count)

# Task 6: Display words in reverse order
print("Words in Reverse Order:")

for word in words[::-1]:
    print(word)

# Task 7: Create a list of unique words
unique_words = list(frequency.keys())
print("Unique Words:", unique_words)
