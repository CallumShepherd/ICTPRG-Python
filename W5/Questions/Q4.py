# Question 4

fullname = input('Enter your full name: ')
splitname = fullname.split()
initials = ''

for i in range(len(splitname)):
    initials += splitname[i][0]
print ('Full name:', fullname)
print('Initials:', initials)