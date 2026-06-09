# . Cricket Tournament Analytics System 
# Problem Statement 
# Store statistics of at least 30 cricket players. 
# Example Structure 
# players = { 
#     "Virat": { 
#         "runs": 645, 
#         "matches": 12, 
#         "wickets": 0 
#     } 
# } 
# Requirements 
# 1. Display all player statistics.  
# 2. Find highest run scorer.  
# 3. Find lowest run scorer.  
# 4. Calculate average runs.  
# 5. Find player with maximum wickets.  
# 6. Find all-rounders (runs > 300 and wickets > 5).  
# 7. Display players scoring above average.  
# 8. Create categories:  
# o Star Performer  
# o Good Performer  
# o Average Performer  
# o Poor Performer  
# 9. Generate team statistics.  
# 10. Display top 5 batsmen.  
# 11. Display top 5 bowlers.  
# 12. Create a separate dictionary for award winners.  
# Challenge 
# Generate a tournament report. 

# Cricket Tournament Analytics System

players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 580, "matches": 12, "wickets": 1},
    "Gill": {"runs": 520, "matches": 11, "wickets": 0},
    "Rahul": {"runs": 410, "matches": 10, "wickets": 0},
    "Hardik": {"runs": 350, "matches": 11, "wickets": 8},
    "Jadeja": {"runs": 330, "matches": 12, "wickets": 10},
    "Ashwin": {"runs": 220, "matches": 10, "wickets": 15},
    "Bumrah": {"runs": 50, "matches": 12, "wickets": 18},
    "Shami": {"runs": 40, "matches": 11, "wickets": 16},
    "Siraj": {"runs": 30, "matches": 12, "wickets": 14}
}

# 1. Display all player statistics
print("Player Statistics:")
for player, stats in players.items():
    print(player, stats)

# 2. Find highest run scorer
highest_runs = max(players, key=lambda x: players[x]["runs"])
print("Highest Run Scorer:")
print(highest_runs, players[highest_runs]["runs"])

# 3. Find lowest run scorer
lowest_runs = min(players, key=lambda x: players[x]["runs"])
print("Lowest Run Scorer:")
print(lowest_runs, players[lowest_runs]["runs"])

# 4. Calculate average runs
total_runs = 0
for stats in players.values():
    total_runs += stats["runs"]

avg_runs = total_runs / len(players)

print("Average Runs:")
print(avg_runs)

# 5. Find player with maximum wickets
max_wickets = max(players, key=lambda x: players[x]["wickets"])
print("Maximum Wickets:")
print(max_wickets, players[max_wickets]["wickets"])

# 6. Find all-rounders (runs > 300 and wickets > 5)
print("All-Rounders:")
for player, stats in players.items():
    if stats["runs"] > 300 and stats["wickets"] > 5:
        print(player)

# 7. Display players scoring above average
print("Players Scoring Above Average:")
for player, stats in players.items():
    if stats["runs"] > avg_runs:
        print(player, stats["runs"])

# 8. Create categories
print("Player Categories:")
for player, stats in players.items():

    if stats["runs"] >= 500:
        category = "Star Performer"

    elif stats["runs"] >= 300:
        category = "Good Performer"

    elif stats["runs"] >= 100:
        category = "Average Performer"

    else:
        category = "Poor Performer"

    print(player, ":", category)

# 9. Generate team statistics
print("Team Statistics:")
print("Total Players:", len(players))

total_wickets = 0
for stats in players.values():
    total_wickets += stats["wickets"]

print("Total Runs:", total_runs)
print("Total Wickets:", total_wickets)

# 10. Display top 5 batsmen
print("Top 5 Batsmen:")
top_batsmen = sorted(players.items(),key=lambda x: x[1]["runs"],reverse=True)

for player, stats in top_batsmen[:5]:
    print(player, stats["runs"])

# 11. Display top 5 bowlers
print("Top 5 Bowlers:")
top_bowlers = sorted(players.items(),key=lambda x: x[1]["wickets"],reverse=True)

for player, stats in top_bowlers[:5]:
    print(player, stats["wickets"])

# 12. Create a separate dictionary for award winners
award_winners = {
    "Best Batsman": highest_runs,
    "Best Bowler": max_wickets
}

print("Award Winners:")
print(award_winners)

# Challenge - Tournament Report
print("Tournament Report")
print("--------------------")
print("Highest Run Scorer:", highest_runs)
print("Highest Runs:", players[highest_runs]["runs"])

print("Best Bowler:", max_wickets)
print("Wickets:", players[max_wickets]["wickets"])

print("Average Runs:", avg_runs)
print("Total Team Runs:", total_runs)
print("Total Team Wickets:", total_wickets)
print("Total Players:", len(players))
