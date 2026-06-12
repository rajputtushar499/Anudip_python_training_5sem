# Student Scholarship Evaluation System 
# Problem Statement 
# The marks obtained by students in the final examination are stored as follows: 
# Sample Data 
# marks = { 
#     "Anuj": 92, 
#     "Rahul": 76, 
#     "Priya": 88, 
#     "Neha": 64, 
#     "Amit": 58, 
#     "Sneha": 95, 
#     "Karan": 81, 
#     "Pooja": 73, 
#     "Rohit": 47, 
#     "Anjali": 90 
# } 
# Tasks 
# 1. Display students scoring above 85 marks.  
# 2. Find the topper.  
# 3. Find the student with the lowest marks.  
# 4. Calculate class average marks.  
# 5. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)  
# 6. Create a list of scholarship students (marks ≥ 90).  
# Sample Output 
# Students Scoring Above 85: 
# Anuj 
# Priya 
# Sneha 
# Anjali 
 
# Topper: 
# Sneha (95) 
 
# Lowest Scorer: 
# Rohit (47) 
 
# Average Marks: 76.4 
 
# Scholarship Students: 
# ['Anuj', 'Sneha', 'Anjali']

#---------------------------------------------------------
# Student Scholarship Evaluation System

marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Students scoring above 85
print("Students Scoring Above 85:")

for student in marks:
    if marks[student] > 85:
        print(student)

# 2. Find topper
highest_marks = 0

for student in marks:
    if marks[student] > highest_marks:
        highest_marks = marks[student]
        topper = student

print("Topper:")
print(topper, highest_marks)

# 3. Find lowest scorer
lowest_marks = 100

for student in marks:
    if marks[student] < lowest_marks:
        lowest_marks = marks[student]
        lowest_student = student

print("Lowest Scorer:")
print(lowest_student,  lowest_marks)

# 4. Calculate average marks
total = 0

for student in marks:
    total = total + marks[student]

average = total / len(marks)

print("Average Marks:", average)

# 5. Generate grades
print("Student Grades:")

for student in marks:
    if marks[student] >= 90:
        grade = "A"
    elif marks[student] >= 75:
        grade = "B"
    elif marks[student] >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", grade)

# 6. Scholarship students
scholarship = []

for student in marks:
    if marks[student] >= 90:
        scholarship.append(student)

print("Scholarship Students:")
print(scholarship)
