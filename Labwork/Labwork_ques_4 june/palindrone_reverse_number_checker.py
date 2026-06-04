# Accept number from user
num = int(input("Enter a number: "))

# Store original number
temp = num

# Variable to store reverse
reverse = 0

# Reverse the number
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# Display reverse number
print("Reverse Number:", reverse)

# Check palindrome
if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
