num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
total = num1 + num2
# Opens file directory & allows writing permission
maths = open('maths.txt', 'w')
# Writes total value to the file as a string
maths.write(str(total))
# Confirmation message
print('Total sum has been output to the file.')
# Closes file
maths.close()