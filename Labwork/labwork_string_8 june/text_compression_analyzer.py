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
# Text Compression Analyzer

text = "AAABBBCCCDDDAAA"

# Task 1 & 2: Character frequency dictionary
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Original Text:", text)

print("Character Frequencies:")
for ch in freq:
    print(ch, "->", freq[ch])

# Task 3: Unique characters
unique_chars = list(freq.keys())
print("Unique Characters:", unique_chars)

# Task 4: Most frequent character
most_frequent = max(freq, key=freq.get)
print("Most Frequent Character:", most_frequent)

# Task 5: Compressed output
compressed = ""

for ch in freq:
    compressed = compressed + ch + str(freq[ch])

print("Compressed Output:", compressed)

# Task 6: Compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(ratio, 2), "%")
