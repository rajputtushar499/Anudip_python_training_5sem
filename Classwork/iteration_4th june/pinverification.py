pin = 1234

entered_pin = int(input("Enter PIN: "))

while entered_pin != pin:
    print("Incorrect PIN. Try Again.")
    entered_pin = int(input("Enter PIN: "))

print("Access Granted.")
