# Social Media Trend Analyzer 
# Problem Statement 
# Trending hashtags collected during an event are stored in a file named hashtags.txt. 
# #AI 
# #Python 
# #AI 
# #MachineLearning 
# #DataScience 
# #Python 
# #AI 
# #Coding 
# #DataScience 
# #Python 
# Tasks 
# 1. Count occurrences of each hashtag.  
# 2. Display the top trending hashtag.  
# 3. Create a set of unique hashtags.  
# 4. Identify hashtags used more than twice.  
# 5. Generate a trend report file.  
# Sample Output 
# Hashtag Frequency: 
# #AI : 3 
# #Python : 3 
# #MachineLearning : 1 
# #DataScience : 2 
# #Coding : 1 
 
# Top Trending Hashtags: 
# #AI 
# #Python 
 
# Unique Hashtags: 
# {'#AI', '#Python', '#MachineLearning', '#DataScience', '#Coding'} 
 
# Hashtags Used More Than Twice: 
# #AI 
# #Python 
 
# Trend Report Generated Successfully.

#--------------------------------------------------
# Task 1: Count Occurrences of Each Hashtag
#--------------------------------------------------

file = open("hashtags.txt", "r")
hashtags = file.read().splitlines()
file.close()

frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

print("Hashtag Frequency:")

for tag, count in frequency.items():
    print(tag, ":", count)


#--------------------------------------------------
# Task 2: Display the Top Trending Hashtag
#--------------------------------------------------

max_count = max(frequency.values())

print("\nTop Trending Hashtags:")

for tag, count in frequency.items():
    if count == max_count:
        print(tag)


#--------------------------------------------------
# Task 3: Create a Set of Unique Hashtags
#--------------------------------------------------

unique_hashtags = set(hashtags)

print("\nUnique Hashtags:")
print(unique_hashtags)


#--------------------------------------------------
# Task 4: Identify Hashtags Used More Than Twice
#--------------------------------------------------

print("\nHashtags Used More Than Twice:")

for tag, count in frequency.items():
    if count > 2:
        print(tag)


#--------------------------------------------------
# Task 5: Generate a Trend Report File
#--------------------------------------------------

file = open("trend_report.txt", "w")

for tag, count in frequency.items():
    file.write(f"{tag} : {count}\n")

file.close()

print("\nTrend Report Generated Successfully.")
