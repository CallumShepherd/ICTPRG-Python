while True:
    InputNumber = input('Enter a number: ')
    if InputNumber.isdigit() == False:
        print('Please enter a valid integer.')
    else:
        print(f'Your number is {InputNumber}.')
        break