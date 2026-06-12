#  Movie Rating Analysis System 
# Problem Statement 
# Ratings given by users for movies are stored below. 
# Sample Data 
# ratings = { 
#     "Inception": 4.8, 
#     "Avatar": 4.3, 
#     "Titanic": 4.5, 
#     "Joker": 4.7, 
#     "Frozen": 3.8, 
#     "Interstellar": 4.9, 
#     "Dune": 4.6, 
#     "Up": 4.1, 
#     "Coco": 4.4, 
#     "Cars": 3.9 
# } 
# Tasks 
# 1. Display movies rated above 4.5.  
# 2. Find the highest-rated movie.  
# 3. Find the lowest-rated movie.  
# 4. Calculate average rating.  
# 5. Create a recommendation list (rating ≥ 4.5).  
# Sample Output 
# Movies Rated Above 4.5: 
# Inception 
# Joker 
# Interstellar 
# Dune 
 
# Highest Rated Movie: 
# Interstellar (4.9) 
 
# Lowest Rated Movie: 
# Frozen (3.8) 
 
# Average Rating: 4.4 
 
# Recommended Movies: 
# ['Inception', 'Titanic', 'Joker', 'Interstellar', 'Dune']

#---------------------------------------------------------
# Movie Rating Analysis System

ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

#---------------------------------------------------------
# 1. Movies rated above 4.5
#---------------------------------------------------------

print("Movies Rated Above 4.5:")

for movie in ratings:
    if ratings[movie] > 4.5:
        print(movie)

#---------------------------------------------------------
# 2. Highest-rated movie
#---------------------------------------------------------

highest_rating = 0

for movie in ratings:
    if ratings[movie] > highest_rating:
        highest_rating = ratings[movie]
        highest_movie = movie

print("Highest Rated Movie:")
print(highest_movie, highest_rating)

#---------------------------------------------------------
# 3. Lowest-rated movie
#---------------------------------------------------------

lowest_rating = 5

for movie in ratings:
    if ratings[movie] < lowest_rating:
        lowest_rating = ratings[movie]
        lowest_movie = movie

print("\nLowest Rated Movie:")
print(lowest_movie,lowest_rating)

#---------------------------------------------------------
# 4. Calculate average rating
#--------------------------------------------------------- 

total = 0

for movie in ratings:
    total = total + ratings[movie]

average = total / len(ratings)

print("Average Rating:", average)

#---------------------------------------------------------
# 5. Recommendation list
#---------------------------------------------------------

recommended = []

for movie in ratings:
    if ratings[movie] >= 4.5:
        recommended.append(movie)

print("Recommended Movies:")
print(recommended)
