# . Student Performance Analytics System
# Problem Statement
# A coaching institute wants to analyze student performance.
# Store details of at least 30 students in a dictionary.
# Example Structure
# students = {
#  "S101": {"name": "Anuj", "marks": 85},
#  "S102": {"name": "Rahul", "marks": 72}
# }
# Requirements
# 1. Display all student records.
# 2. Search a student using Student ID.
# 3. Add a new student.
# 4. Update marks of an existing student.
# 5. Delete a student.
# 6. Find topper and lowest scorer.
# 7. Calculate class average.
# 8. Count pass and fail students.
# 9. Generate grades:
# o A (90+)
# o B (75–89)
# o C (50–74)
# o F (<50)
# 10. Display students scoring above average.
# 11. Display top 5 performers.
# 12. Create a separate dictionary for scholarship students (marks > 85).
# Expected Learning
# • Nested Dictionaries
# • Dictionary Traversal
# • Searching
# • Aggregation
# • Report Generation 

# . Student Performance Analytics System
# Problem Statement
# A coaching institute wants to analyze student performance.
# Store details of at least 30 students in a dictionary.
# Example Structure
# students = {
#  "S101": {"name": "Anuj", "marks": 85},
#  "S102": {"name": "Rahul", "marks": 72}
# }
# Requirements
# 1. Display all student records.
# 2. Search a student using Student ID.
# 3. Add a new student.
# 4. Update marks of an existing student.
# 5. Delete a student.
# 6. Find topper and lowest scorer.
# 7. Calculate class average.
# 8. Count pass and fail students.
# 9. Generate grades:
# o A (90+)
# o B (75–89)
# o C (50–74)
# o F (<50)
# 10. Display students scoring above average.
# 11. Display top 5 performers.
# 12. Create a separate dictionary for scholarship students (marks > 85).
# Expected Learning
# • Nested Dictionaries
# • Dictionary Traversal
# • Searching
# • Aggregation
# • Report Generation 

# Student Performance Analytics System

students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Aman", "marks": 91},
    "S104": {"name": "Priya", "marks": 67},
    "S105": {"name": "Karan", "marks": 49},
    "S106": {"name": "Neha", "marks": 95},
    "S107": {"name": "Rohit", "marks": 78},
    "S108": {"name": "Pooja", "marks": 88},
    "S109": {"name": "Vikas", "marks": 55},
    "S110": {"name": "Simran", "marks": 92},
    "S111": {"name": "Arjun", "marks": 61},
    "S112": {"name": "Nisha", "marks": 83},
    "S113": {"name": "Deepak", "marks": 74},
    "S114": {"name": "Riya", "marks": 89},
    "S115": {"name": "Sahil", "marks": 44},
    "S116": {"name": "Kavya", "marks": 96},
    "S117": {"name": "Harsh", "marks": 58},
    "S118": {"name": "Meena", "marks": 81},
    "S119": {"name": "Yash", "marks": 69},
    "S120": {"name": "Tanvi", "marks": 97},
    "S121": {"name": "Aryan", "marks": 77},
    "S122": {"name": "Muskan", "marks": 84},
    "S123": {"name": "Nitin", "marks": 52},
    "S124": {"name": "Sneha", "marks": 90},
    "S125": {"name": "Manav", "marks": 65},
    "S126": {"name": "Isha", "marks": 87},
    "S127": {"name": "Aditi", "marks": 93},
    "S128": {"name": "Gaurav", "marks": 48},
    "S129": {"name": "Tina", "marks": 79},
    "S130": {"name": "Rakesh", "marks": 71}
}

# 1. Display all student records
print("Student Records:")
for sid in students:
    print(sid, students[sid])
# 2. Search a student using Student ID
search_id = input("Enter Student ID to Search: ")

if search_id in students:
    print(students[search_id])
else:
    print("Student Not Found")

# 3. Add a new student
sid = input("Enter New Student ID: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

students[sid] = {"name": name, "marks": marks}

# 4. Update marks of an existing student
update_id = input("Enter Student ID to Update Marks: ")

if update_id in students:
    new_marks = int(input("Enter New Marks: "))
    students[update_id]["marks"] = new_marks
    print("Marks Updated")
else:
    print("Student Not Found")

# 5. Delete a student
delete_id = input("Enter Student ID to Delete: ")

if delete_id in students:
    del students[delete_id]
    print("Student Deleted")
else:
    print("Student Not Found")

# 6. Find topper and lowest scorer
topper = max(students, key=lambda x: students[x]["marks"])
lowest = min(students, key=lambda x: students[x]["marks"])

print("Topper:", topper, students[topper])
print("Lowest Scorer:", lowest, students[lowest])

# 7. Calculate class average
total = 0

for sid in students:
    total += students[sid]["marks"]

average = total / len(students)

print("\nClass Average:", round(average, 2))

# 8. Count pass and fail students
pass_count = 0
fail_count = 0

for sid in students:
    if students[sid]["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

# 9. Generate grades
print("Grades:")

for sid in students:
    marks = students[sid]["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, students[sid]["name"], ":", grade)

# 10. Students scoring above average
print("Students Above Average:")

for sid in students:
    if students[sid]["marks"] > average:
        print(sid, students[sid])

# 11. Top 5 performers
print("Top 5 performers")
top5 = sorted(students.items(),key=lambda student: student[1]["marks"],reverse=True)

# Display first 5 students
for student in top5[:5]:
    print(student)
# 12. Scholarship students (marks > 85)
scholarship = {}

for sid in students:
    if students[sid]["marks"] > 85:
        scholarship[sid] = students[sid]

print("\nScholarship Students:")
for sid in scholarship:
    print(sid, scholarship[sid])
