#  Cricket Tournament Statistics 
# Problem Statement 
# Runs scored by players in a tournament are given below. 
# Sample Data 
# runs = { 
#     "Virat": 645, 
#     "Rohit": 512, 
#     "Gill": 698, 
#     "Rahul": 435, 
#     "Hardik": 278, 
#     "Pant": 534, 
#     "Surya": 389, 
#     "Jadeja": 301, 
#     "Iyer": 455, 
#     "KL": 410 
# } 
# Tasks 
# 1. Find the Orange Cap winner.  
# 2. Find the lowest scorer.  
# 3. Calculate total runs scored.  
# 4. Display players scoring more than 500 runs.  
# 5. Create a list of players scoring below 400.  
# Sample Output 
# Orange Cap Winner: 
# Gill (698 runs) 
 
# Lowest Scorer: 
# Hardik (278 runs) 
 
# Total Runs: 4657 
 
# Players Scoring Above 500: 
# Virat 
# Rohit 
# Gill 
# Pant 
 
# Players Scoring Below 400: 
# ['Hardik', 'Surya', 'Jadeja']

#---------------------------------------------------
# Cricket Tournament Statistics

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#---------------------------------------------------------
# 1. Orange Cap Winner
#----------------------------------------------------------

highest_runs = 0

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        top_player = player

print("Orange Cap Winner:")
print(top_player, highest_runs, "runs")

#---------------------------------------------------------
# 2. Lowest Scorer
#---------------------------------------------------------

lowest_runs = 1000

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        low_player = player

print("Lowest Scorer:")
print(low_player, lowest_runs, "runs")

#---------------------------------------------------------
# 3. Calculate Total Runs
#---------------------------------------------------------

total_runs = 0

for player in runs:
    total_runs = total_runs + runs[player]

print("Total Runs:", total_runs)

#----------------------------------------------------------
# 4. Players Scoring More Than 500 Runs
#----------------------------------------------------------

print("Players Scoring Above 500:")

for player in runs:
    if runs[player] > 500:
        print(player)

#------------------------------------------------------------
# 5. Players Scoring Below 400 Runs
#-------------------------------------------------------------

below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("Players Scoring Below 400:")
print(below_400)
