with open ( 'data.txt', 'w') as f1:
    while True:
        product_id=input('Product ID: ')
        if product_id == '':
            break
        print(product_id)
        name = input ('Item Name: ')
        print(name)
        price = input('Price: ')
        print(f'${price.strip("$")}')
        f1.write(product_id + '\n')
        f1.write(name + '\n')
        f1.write(price.strip('$') + '\n')
 
with open('data.txt','r') as f2:
    items=f2.readlines()
print(items)
sum = 0
for i in range(1, len(items) + 1):
    # picking up the third item in the array. The range is changed to use the code i%3 
    #since index starts with 0
    if i % 3 ==0:
        price=float(items[i-1])
        print(f'The index is {i - 1}.')
        print(f'The price is ${price}.')
        sum = sum + price
print (f'The sum of the prices is ${sum}.')