# Question 4

user = input('Enter username: ')
password = input('Enter password: ')

if (user == 'bob'):
    if (password == 'password1234'):
        print('Access granted!')
    else:
        print('Access denied.')
elif (user == 'fred'):
    if (password == 'happyPass122'):
        print('Access granted!')
    else:
        print('Access denied.')
elif (user == 'lock'):
    if (password == 'passwithlock44'):
        print('Access granted!')
    else:
        print('Access denied.')
else:
    print('Invalid username.')