# Question 3 v2

username0 = 'bob'
password0 = 'password1234'
username1 = 'frank'
password1 = 'invalidpass'
username2 = 'lock'
password2 = 'password2468'

userInput0 = input('What is your username?: ')

if (userInput0 == username0):
    userInput1 = input('Please enter your password: ')
    if (userInput1 == password0):
        print('Access granted!')
    else:
        print('Access denied.')
elif (userInput0 == username1):
    userInput1 = input('Please enter your password: ')
    if (userInput1 == password1):
        print('Access granted!')
    else:
        print('Access denied.')
elif (userInput0 == username2):
    userInput1 = input('Please enter your password: ')
    if (userInput1 == password2):
        print('Access granted!')
    else:
        print('Access denied.')
else:
    print('Invalid username.')