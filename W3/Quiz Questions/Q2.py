# Question 2

year = int(input('What is your year of birth?: '))
age = 2021 - year

print('You are ' + str(age) + ' years old.')

if (age >= 18):
    print('Come in and have a drink!')
else:
    print('Please leave, you are not old enough.')