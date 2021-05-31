salary = float(input('What is your salary?: $'))
time = int(input('How many years have you worked at the company?: '))

if (salary >= 50000 and time >= 3):
    print('You are eligible for a loan.')
else:
    print('You are not eligible for a loan.')