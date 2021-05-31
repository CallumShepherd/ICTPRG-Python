# Question 5

number = input('Enter a number (x to stop): ')
number_list = []

while number != 'x':
    number_list.append(number)
    number = input('Enter a number (x to stop): ')

print('You entered:', number_list)