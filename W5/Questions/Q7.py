# Question 7

nums = []
dups = []
num = input('Enter a number (x to stop): ')

while (num != 'x'):
    if (int(num) in nums):
        nums.append(int(num))
        dups.append(int(num))
    else:
        nums.append(int(num))
    num = input('Enter a number (x to stop): ')

print('Duplicate numbers:', dups)

# WEB ANSWER 1

# def findDuplicates(x):
#     # Define how many values are in the numbers list (e.g. 3)
#     size = len(x)
#     # Create an empty list that holds the values that are duplicated in the numbers list
#     repeats = []
#     # Loop through the range of the numbers list size (0-2), with i being one of those values (0, 1 or 2)
#     for i in range(size):
#         # Every loop through i, k is defined as being as 1 more than i (i + 1)
#         k = i + 1
#         # Loop through the range of (i + 1) being the lower value, and size (the number of values in the numbers list) being the higher value
#         # In the example where size = 3, i[0] means that k = 1, i[1] means that k = 2, so on and so forth
#         # First loop goes through a range of 1-3, second loop goes through a range of 2-3, third loop goes through a range of 3-3.
#         # In total, the ranges go through as [1], [2], [3], [2], [3], [3]
#         for j in range(k, size):
#             # Conditional: if the index of an element in the numbers list == the index of an element list in numbers 
#             if x[i] == x[j] and x[i] not in repeats:
#                 repeats.append(x[i])
#     return repeats

# number = input('Enter a number (x to stop): ')
# numbers = []
# while number != 'x':
#     numbers.append(number)
#     number = input('Enter a number (x to stop): ')

# print('Repeating numbers:', '[%s]' % ', '.join(map(str, findDuplicates(numbers))))

# WEB ANSWER 2

# number = input('Enter a number (x to stop): ')
# numbers = []
# while number != 'x':
#     numbers.append(number)
#     number = input('Enter a number (x to stop): ')

# dupItems = []
# uniqItems = {}

# for x in numbers:
#     if x not in uniqItems:
#         uniqItems[x] = 1
#     else:
#         if uniqItems[x] == 1:
#             dupItems.append(x)
#         uniqItems[x] += 1

# print('Repeating numbers:', dupItems)

# LUCAS ANSWER

# array = []
# dupes = []

# while True:
#     num = input('Gimme number: ')
#     if num == 'x':
#         break
#     if int(num) in array:
#         array.append(int(num))
#         dupes.append(int(num))
#     else:
#         array.append(int(num))

# print('Numbers:', array)
# print('Duplicates:', dupes)