# Question 6

num = input('Enter number to add: ')
numList = []

for i in range(len(num)):
    numList.append(int(num[i]))

added = sum(numList)

print('Sum of the digits:', end=' ')
for i in range(len(numList)-1):
    print(numList[i], '+', end=' ')
print(numList[-1], '=', added)