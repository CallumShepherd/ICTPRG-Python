import math

num = 1
start = range(1, num + 1)
num_range = range(0, 10)

for x in start:
    for num in num_range:
        num += 1
        output = math.factorial(num)
        print(f'{num}! = {output}')