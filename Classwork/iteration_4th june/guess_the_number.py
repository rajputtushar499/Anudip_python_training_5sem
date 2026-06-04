secret_number = 7

guess = int(input("Guess the Number: "))

while guess != secret_number:
    print("Wrong Guess. Try Again.")
    guess = int(input("Guess the Number: "))

print("Congratulations! You guessed the correct number.")
