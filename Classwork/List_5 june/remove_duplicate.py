numbers = []

# Input 20 numbers from the user
for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Create an empty list to store unique numbers
unique_numbers = []

# Check each number in the original list
for num in numbers:

    # Add the number only if it is not already present
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display the list after removing duplicates
print("List after removing duplicates:")
print(unique_numbers)

