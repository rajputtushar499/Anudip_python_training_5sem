#  Word Frequency Analyzer 
# Problem Statement 
# A text file contains the following paragraph. 
# Sample Input/Data (article.txt) 
# Python is easy to learn. 
# Python is powerful. 
# Python supports multiple programming paradigms. 
# Programming with Python is enjoyable. 
# Tasks 
# 1. Count the total number of words.  
# 2. Count the frequency of each word.  
# 3. Find the most frequently occurring word.  
# 4. Display words appearing only once.  
# 5. Display all unique words.  
# Sample Output 
# Total Words: 16 
 
# Most Frequent Word: 
# Python (4 times) 
 
# Words Appearing Once: 
# easy 
# to 
# learn 
# powerful 
# supports 
# multiple 
# paradigms 
# with 
# enjoyable 
 
# Unique Words Count: 12 

#--------------------------------------------------
# Task 1: Count Total Number of Words
#--------------------------------------------------

file = open("article.txt", "r")
content = file.read().lower()
file.close()

content = content.replace(".", "")
words = content.split()

print("Total Words:", len(words))


#--------------------------------------------------
# Task 2: Count Frequency of Each Word
#--------------------------------------------------

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1


#--------------------------------------------------
# Task 3: Find Most Frequently Occurring Word
#--------------------------------------------------

max_word = ""
max_count = 0

for word, count in frequency.items():
    if count > max_count:
        max_count = count
        max_word = word

print("\nMost Frequent Word:")
print(max_word, "(", max_count, "times )")


#--------------------------------------------------
# Task 4: Display Words Appearing Only Once
#--------------------------------------------------

print("\nWords Appearing Once:")

for word, count in frequency.items():
    if count == 1:
        print(word)


#--------------------------------------------------
# Task 5: Display All Unique Words
#--------------------------------------------------

print("\nUnique Words Count:", len(frequency))

