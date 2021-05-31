# Import re, allows for more string manipulation
import re

while True:
# Variables reset after each iteration
    GetPassword = input("Enter a solid password: ")
    flag = 0
    reasons = []

# Validation through if statements
    # integer is missing
    if not re.search("[0-9]", GetPassword):
        flag = -1
        reasons.append("Integer is missing.")
    # lowercase letter is missing
    if not re.search("[a-z]", GetPassword):
        flag = -1
        reasons.append("Lowercase letter is missing.")
    # uppercase letter is missing
    if not re.search("[A-Z]", GetPassword):
        flag = -1
        reasons.append("Uppercase letter is missing.")
    # special character is missing
    if not re.search("[_!@#$%^&*()+=;:.,/?\'\"]", GetPassword):
        flag = -1
        reasons.append("Special character is missing.")
    # password is too short (<7 characters long)
    if len(GetPassword) < 7:
        flag = -1
        reasons.append("Password length must be equal to or more than 7 characters.")
    # password is not strong enough ("password")
    if GetPassword.lower() == 'password':
        flag = -1
        reasons.append("The password 'password' is not strong enough.")

# If password is invalid, tell user and list reasons
    if flag == -1:
        print("\nPassword is invalid.")
        print("Reasons:")
        for listElement in reasons:
            print("-", listElement)
        print("")

# If password is valid, ask user to confirm password.
    else:
        confirm = input("Confirm your password: ")
        if confirm == GetPassword:
            print("\nValid password.\n")
            break
        else:
            print("\nPasswords do not match.\n")