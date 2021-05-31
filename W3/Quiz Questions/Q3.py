# Question 3

user = input('Enter username: ')
password = input('Enter password: ')

if (user == 'bob'):
    if (password == 'password1234'):
        print('Access granted!')
    else:
        print('Access denied.')
else:
    print('Invalid username.')