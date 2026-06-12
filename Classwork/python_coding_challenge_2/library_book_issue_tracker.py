# Library Book Issue Tracker 
# Problem Statement 
# A library stores the number of times books were issued during a month. 
# Sample Data 
# book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
# Tasks 
# 1. Find the maximum number of issues.  
# 2. Find the minimum number of issues.  
# 3. Calculate the average number of issues.  
# 4. Count books issued more than 15 times.  
# 5. Create a list of books issued fewer than 10 times.  
# Sample Output 
# Maximum Issues: 30 
 
# Minimum Issues: 5 
 
# Average Issues: 16.5 
 
# Books Issued More Than 15 Times: 5 
 
# Books Issued Fewer Than 10 Times: 
# [8, 5]

#-------------------------------------------------------------
# Library Book Issue Tracker
#-------------------------------------------------------------

book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

#-------------------------------------------------------------
# Task 1 Find the maximum number of issues
#-------------------------------------------------------------

maximum = book_issues[0]

for issue in book_issues:
    if issue > maximum:
        maximum = issue

print("Maximum Issues:", maximum)

#--------------------------------------------------------------
# Task 2 Find the minimum number of issues
#--------------------------------------------------------------

minimum = book_issues[0]

for issue in book_issues:
    if issue < minimum:
        minimum = issue

print("\nMinimum Issues:", minimum)

#-------------------------------------------------------------
# Task 3 Calculate the average number of issues
#-------------------------------------------------------------

total = 0

for issue in book_issues:
    total = total + issue

average = total / len(book_issues)

print("\nAverage Issues:", average)

#--------------------------------------------------------------
# Task 4 Count books issued more than 15 times
#--------------------------------------------------------------

count = 0

for issue in book_issues:
    if issue > 15:
        count = count + 1

print("\nBooks Issued More Than 15 Times:", count)

#----------------------------------------------------------
# Task 5 Create a list of books issued fewer than 10 times
#----------------------------------------------------------

less_than_10 = []

for issue in book_issues:
    if issue < 10:
        less_than_10.append(issue)

print("\nBooks Issued Fewer Than 10 Times:")
print(less_than_10)
