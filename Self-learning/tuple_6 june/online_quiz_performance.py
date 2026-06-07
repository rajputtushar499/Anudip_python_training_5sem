# Online Quiz Performance
# Sample Data
# quiz_scores = { 
# "S001": 18, 
# "S002": 12, 
# "S003": 9, 
# "S004": 20,
# "S005": 14, 
# "S006": 7, 
# "S007": 16,
# "S008": 10, 
# "S009": 19, 
# "S010": 13
# }
# (Quiz is out of 20 marks.)
# Tasks
# Display students scoring 15 or above.
# Count students scoring below 10.
# Find the top performer.
# Create a list of students who passed (≥ 10 marks).
# Calculate the class average.

# Quiz Scores Dictionary
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Students scoring 15 or above
print("Students scoring 15 or above:")
for student in quiz_scores:
    if quiz_scores[student] >= 15:
        print(student, quiz_scores[student])

# Count students scoring below 10
count = 0

for student in quiz_scores:
    if quiz_scores[student] < 10:
        count += 1

print("Students scoring below 10:", count)

# Find top performer
top_student = ""
top_score = 0

for student in quiz_scores:
    if quiz_scores[student] > top_score:
        top_score = quiz_scores[student]
        top_student = student

print("Top Performer:")
print(top_student, top_score)

# List of students who passed
passed = []

for student in quiz_scores:
    if quiz_scores[student] >= 10:
        passed.append(student)

print("Students who Passed:")
print(passed)

# Calculate class average
total = 0

for student in quiz_scores:
    total += quiz_scores[student]

average = total / len(quiz_scores)

print("Class Average:", average)
