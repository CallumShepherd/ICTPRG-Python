A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input('What is your score out of 100?: '))

if score >= A_score:
    print('your grade is A')
else:
    if score >= B_score:
        print('Your grade is B')
    else:
        if score >= C_score:
            print('your grade is C')
        else:
            if score >= D_score:
                print('Your grade is D')
            else:
                print('your grade is F')