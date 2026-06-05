# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store consecutive pairs
consecutive_pairs = []

# Loop through the list up to the second last element
for i in range(len(numbers) - 1):

    # Check if the next number is exactly 1 greater
    if numbers[i + 1] == numbers[i] + 1:

        # Display the consecutive pair
        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store the pair as a tuple in the new list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Display all consecutive pairs
print("Consecutive Pairs:", consecutive_pairs)
