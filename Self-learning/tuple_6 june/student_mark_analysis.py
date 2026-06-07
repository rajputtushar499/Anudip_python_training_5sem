# Student Marks Analysis
# Sample Data
# marks = {
#          "Aarav": 78,
#          "Diya": 92,
#          "Rohan": 45,
#          "Ishita": 88,
#          "Kabir": 56,
#          "Meera": 39,
#          "Arjun": 95,
#          "Saanvi": 67,
#          "Vivaan": 82,
#          "Anaya": 51
#         }
# Tasks
# Display students scoring 80 or above.
# Count the number of students who failed (marks < 40).
# Find the highest scorer.
# Create a list of students scoring between 60 and 75.
# Assign grades:
# A: ≥ 90
# B: 75–89
# C: 50–74
# F: < 50

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}
# 1. Display students scoring 80 or above
print("Students scoring 80 or above:")  
for mark in marks:
    if marks[mark] >= 80:
        print(mark, marks[mark])
# 2. Count the number of students who failed (marks < 40)
fail_count = 0
for mark in marks:
    if marks[mark] < 40:
        fail_count += 1
print("Number of students who failed:", fail_count)
# 3. Find the highest scorer
highest_marks = 0

for mark in marks:
    if marks[mark] > highest_marks:
        highest_marks = marks[mark]
        highest_name = mark

print("Highest Scorer:")
print(highest_name, highest_marks)
# 4. Create a list of students scoring between 60 and 75
students = []
for mark in marks:
    if marks[mark] >= 60 and marks[mark] <= 75:
        students.append(mark)
print("Students scoring between 60 and 75:")
print(students)  
# 5. Assign grades
print("Grades:")
for mark in marks:
    score = marks[mark]
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(mark, "->", grade)
