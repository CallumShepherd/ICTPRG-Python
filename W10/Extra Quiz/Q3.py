userInput = str(input("Enter some random characters: "))

if len(userInput) > 7:
    print(userInput[int(len(userInput) / 2 - 1):int(len(userInput) / 2 + 2)])
else:
    print(userInput)