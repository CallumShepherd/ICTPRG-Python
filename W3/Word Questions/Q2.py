score1 = int(input('Enter first score here: '))
score2 = int(input('Enter second score here: '))
score3 = int(input('Enter third score here: '))
average = float((score1+score2+score3)/3)

if (average >= 90):
    print('You scored' + str(average) + 'and a grade of A.')
elif (average >=80):
    print('You scored ' + str(average) + ' and a grade of B.')
elif (average >=70):
    print('You scored ' + str(average) + ' and a grade of C.')
elif (average >=60):
    print('You scored ' + str(average) + ' and a grade of D.')
else:
    print('You scored ' + str(average) + ' and a grade of F.')