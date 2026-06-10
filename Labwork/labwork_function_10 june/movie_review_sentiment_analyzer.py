# Movie Review Sentiment Analyzer 
# Problem Statement 
# Movie reviews are stored as follows: 
# reviews = [ 
#     "excellent movie", 
#     "average story", 
#     "excellent acting", 
#     "poor direction", 
#     "excellent visuals", 
#     "poor screenplay", 
#     "good music", 
#     "excellent climax", 
#     "average performance", 
#     "good cinematography" 
# ] 
# Requirements 
# Create the following functions: 
# 1. count_sentiments(reviews) 
# Counts: 
# • Excellent  
# • Good  
# • Average  
# • Poor reviews  
# 2. most_common_word(reviews) 
# Returns the most frequently occurring word. 
# 3. longest_review(reviews) 
# Returns the review containing the maximum number of characters. 
# 4. reviews_with_keyword(reviews, keyword) 
# Displays all reviews containing a given keyword. 
# Sample Output 
# Excellent Reviews: 4 
# Good Reviews: 2 
# Average Reviews: 2 
# Poor Reviews: 2 
 
# Most Common Word: 
# excellent 
 
# Longest Review: 
# good cinematography 
 
# Reviews containing 'excellent': 
# excellent movie 
# excellent acting 
# excellent visuals 
# excellent climax

# Movie reviews list
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# ---------------- TASK 1 ----------------
# Count different sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for r in reviews:
        if "excellent" in r:
            excellent += 1
        elif "good" in r:
            good += 1
        elif "average" in r:
            average += 1
        elif "poor" in r:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)

# ---------------- TASK 2 ----------------
# Most common word
def most_common_word(reviews):
    words = []
    for r in reviews:
        words.extend(r.split())

    most_common = max(set(words), key=words.count)
    print("\nMost Common Word:")
    print(most_common)

# ---------------- TASK 3 ----------------
# Longest review
def longest_review(reviews):
    longest = max(reviews, key=len)
    print("\nLongest Review:")
    print(longest)

# ---------------- TASK 4 ----------------
# Reviews containing keyword
def reviews_with_keyword(reviews, keyword):
    print(f"\nReviews containing '{keyword}':")
    for r in reviews:
        if keyword in r:
            print(r)

# ---------------- MAIN PROGRAM ----------------
count_sentiments(reviews)
most_common_word(reviews)
longest_review(reviews)

reviews_with_keyword(reviews, "excellent")
