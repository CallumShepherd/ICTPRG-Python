user = input('Enter username: ')
password = input('Enter password: ')

with open('logins.txt', 'r') as logins:
    login = logins.read()
    login_split = login.split(':')
    if user == login_split[0] and password == login_split[1]:
        print('Access granted!')
    else:
        print('Access denied.')