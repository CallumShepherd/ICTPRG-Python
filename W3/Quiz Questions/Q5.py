# Question 5

grade = int(input('What is your grade?: '))

if (grade >= 90 and grade <= 100):
    print('You will recieve a High Distinction.')
elif (grade >= 80 and grade < 90):
    print('You will recieve a Distinction.')
elif (grade >= 70 and grade < 80):
    print('You will recieve a Credit.')
elif (grade >= 50 and grade < 70):
    print('You will recieve a Pass.')
elif (grade < 50 and grade >= 0):
    print('You will recieve a Fail.')
else:
    print('Enter a valid grade.')