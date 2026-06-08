# Text Compression Analyzer
# Problem Statement
# A compressed message is given:
# AAABBBCCCDDDAAA
# Tasks
# Write a program to:
# 1.Count occurrences of each character.
# 2.Create a dictionary of character frequencies.
# 3.Display unique characters.
# 4.Find the most frequent character.
# 5.Create a compressed output:
# A3B3C3D3A3
# 6.Calculate compression ratio.
# Sample Output
# Original Text: 
# AAABBBCCCDDDAAA 
# Character Frequencies:
# A -> 6
# B -> 3
# C -> 3
# D -> 3
# Unique Characters:
# ['A', 'B', 'C', 'D']
# Most Frequent Character: A 
# Compressed Output: A3B3C3D3A3
# Original Length: 15
# Compressed Length: 10
# Compression Ratio: 66.67%

# Text Compression Analyzer

text = "AAABBBCCCDDDAAA"

# Task 1 & 2: Count occurrences and create frequency dictionary
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequencies:")
for ch in freq:
    print(ch, "->", freq[ch])

# Task 3: Display unique characters
unique_chars = list(freq.keys())
print("Unique Characters:", unique_chars)

# Task 4: Find most frequent character
most_frequent = max(freq, key=freq.get)
print("Most Frequent Character:", most_frequent)

# Task 5: Create compressed output
compressed = ""
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed = compressed + text[i] + str(count)
        count = 1

compressed = compressed + text[-1] + str(count)

print("Compressed Output:", compressed)

# Task 6: Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", ratio, "%")
