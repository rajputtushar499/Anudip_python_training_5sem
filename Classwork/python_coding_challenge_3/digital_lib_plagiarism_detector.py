# : Digital Library Plagiarism Detector 
# Problem Statement 
# Two research abstracts are provided as strings. 
# abstract1 = "Artificial intelligence is transforming education and healthcare." 
# abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence." 
# Tasks 
# 1. Convert both abstracts into sets of words.  
# 2. Identify common words.  
# 3. Identify unique words in each abstract.  
# 4. Calculate the percentage similarity.  
# 5. Display whether plagiarism review is required (similarity > 50%).  
# Sample Output 
# Common Words: 
# {'artificial', 'intelligence', 'education', 'healthcare'} 
 
# Unique Words in Abstract 1: 
# {'is', 'transforming', 'and'} 
 
# Unique Words in Abstract 2: 
# {'are', 'rapidly', 'through', 'transforming'} 
 
# Similarity Percentage: 
# 50.0% 
 
# Plagiarism Review Required: 
# No

#--------------------------------------------------
# Task 1: Convert Both Abstracts into Sets of Words
#--------------------------------------------------

abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

words1 = set(abstract1.lower().replace(".", "").split())
words2 = set(abstract2.lower().replace(".", "").split())


#--------------------------------------------------
# Task 2: Identify Common Words
#--------------------------------------------------

common_words = words1.intersection(words2)

print("Common Words:")
print(common_words)


#--------------------------------------------------
# Task 3: Identify Unique Words in Each Abstract
#--------------------------------------------------

unique_abstract1 = words1 - words2
unique_abstract2 = words2 - words1

print("\nUnique Words in Abstract 1:")
print(unique_abstract1)

print("\nUnique Words in Abstract 2:")
print(unique_abstract2)


#--------------------------------------------------
# Task 4: Calculate the Percentage Similarity
#--------------------------------------------------

similarity = (len(common_words) / len(words1.union(words2))) * 100

print("\nSimilarity Percentage:")
print(round(similarity, 1), "%", sep="")


#--------------------------------------------------
# Task 5: Display Whether Plagiarism Review is Required
#--------------------------------------------------

print("\nPlagiarism Review Required:")

if similarity > 50:
    print("Yes")
else:
    print("No")
