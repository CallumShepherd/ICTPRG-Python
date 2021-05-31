total = 0.0

num = float(input('Enter a number to add to the total (enter \'x\' to finish): '))
while (num != 'x'):
    total = total + float(num)
    num = input('Enter another number: ')

print('Total: ' + str(total))

# total = 0.0
# count = 1

# num = float(input('Enter number ' + str(count) + ' to add to the total (enter \'x\' to finish): '))
# while (num != str('x')):
#     total = total + float(num)
#     count += 1
#     num = input('Enter number ' + str(count) + ' to add to the total (enter \'x\' to finish): ')

# print('Total: ' + str(total))