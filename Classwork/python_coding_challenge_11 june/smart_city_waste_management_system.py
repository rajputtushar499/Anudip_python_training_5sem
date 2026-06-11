#  Smart City Waste Collection Management System 
# Problem Statement 
# The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
# Sample Data 
#     "Sector2": 180, 
#     "Sector3": 510, 
#     "Sector4": 275, 
#     "Sector5": 150, 
#     "Sector6": 430, 
#     "Sector7": 220, 
#     "Sector8": 390, 
#     "Sector9": 145, 
#     "Sector10": 600 
# } 
# Tasks 
# 1. Display sectors generating more than 400 kg of waste.  
# 2. Find the sector generating maximum waste.  
# 3. Find the sector generating minimum waste.  
# 4. Calculate the total waste collected.  
# 5. Categorize sectors:  
# o Low Waste (<200 kg)  
# o Medium Waste (200–400 kg)  
# o High Waste (>400 kg)  
# 6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
# 7. Save the awareness campaign list to campaign_sectors.txt.  
# Sample Output 
# Sectors Generating More Than 400 kg Waste: 
# Sector3 
# Sector6 
# Sector10 
 
# Maximum Waste Generation: 
# Sector10 (600 kg) 
 
# Minimum Waste Generation: 
# Sector9 (145 kg) 
 
# Total Waste Collected: 3220 kg 
 
# Low Waste: 
# ['Sector2', 'Sector5', 'Sector9'] 
 
# Medium Waste: 
# ['Sector1', 'Sector4', 'Sector7', 'Sector8'] 
 
# High Waste: 
# ['Sector3', 'Sector6', 'Sector10'] 
 
# Sectors Requiring Awareness Campaign: 
# Sector1 
# Sector3 
# Sector6 
# Sector8 
# Sector10 
 
# Campaign Report Generated Successfully.

#--------------------------------------------------------------------
# Smart City Waste Collection Management System

# Dictionary storing waste collected from sectors
waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# --------------------------------------------------
# Task 1: Display Sectors Generating More Than 400 kg Waste
# --------------------------------------------------

print("Sectors Generating More Than 400 kg Waste:")

for sector, kg in waste.items():

    if kg > 400:
        print(sector)

# --------------------------------------------------
# Task 2: Find Sector Generating Maximum Waste
# --------------------------------------------------

max_sector = max(waste, key=waste.get)

print("\nMaximum Waste Generation:")
print(max_sector, "(", waste[max_sector], "kg )")

# --------------------------------------------------
# Task 3: Find Sector Generating Minimum Waste
# --------------------------------------------------

min_sector = min(waste, key=waste.get)

print("\nMinimum Waste Generation:")
print(min_sector, "(", waste[min_sector], "kg )")

# --------------------------------------------------
# Task 4: Calculate Total Waste Collected
# --------------------------------------------------

total = 0

for kg in waste.values():
    total += kg

print("\nTotal Waste Collected:", total, "kg")

# --------------------------------------------------
# Task 5: Categorize Sectors
# --------------------------------------------------

low = []
medium = []
high = []

for sector, kg in waste.items():

    if kg < 200:
        low.append(sector)

    elif kg <= 400:
        medium.append(sector)

    else:
        high.append(sector)

print("\nLow Waste:")
print(low)

print("\nMedium Waste:")
print(medium)

print("\nHigh Waste:")
print(high)

# --------------------------------------------------
# Task 6: Count Sectors Requiring Awareness Campaign
# --------------------------------------------------

campaign_list = []

for sector, kg in waste.items():

    if kg > 300:
        campaign_list.append(sector)

print("\nSectors Requiring Awareness Campaign:")

for sector in campaign_list:
    print(sector)

# --------------------------------------------------
# Task 7: Save Campaign List to File
# --------------------------------------------------

file = open("campaign_sectors.txt", "w")

for sector in campaign_list:
    file.write(sector + "\n")

file.close()

print("\nCampaign Report Generated Successfully.")
