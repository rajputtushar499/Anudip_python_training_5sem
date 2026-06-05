# Store student marks in a list
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Create empty lists and variables
passed = []
merit = []
failed = 0

# Assume first mark is highest and lowest
highest = marks[0]
lowest = marks[0]

# Check each mark
for mark in marks:

    # Check pass students
    if mark >= 40:
        passed.append(mark)
    else:
        failed = failed + 1

    # Find highest mark
    if mark > highest:
        highest = mark

    # Find lowest mark
    if mark < lowest:
        lowest = mark

    # Create merit list
    if mark > 75:
        merit.append(mark)

# Display results
print("Passed Students:", passed)
print("Failed Count:", failed)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)
