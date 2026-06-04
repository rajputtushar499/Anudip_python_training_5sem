password = "admin123"

user_password = input("Enter Password: ")

while user_password != password:
    print("Invalid Password.")
    user_password = input("Enter Password: ")

print("Login Successful.")
