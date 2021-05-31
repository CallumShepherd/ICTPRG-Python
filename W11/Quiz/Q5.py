# Write a program called 'GetWordsFromUser' that takes a Min and Max as a parameter.
# The function then takes an input from the user and ensures that the input has
# at least or at most the specified amount of words.
# Keep on asking the user until the amount of words is within range,
# the program then outputs all words lowercase and separated in a list.

def GetWordsFromUser(min, max):
    print(f"Range permitted: {min} to {max} words.")
    while True:
        userInput = input("Input a number of words within the range specified: ")
        lowerCaseInput = userInput.lower()
        inputList = lowerCaseInput.split()
        if len(inputList) > max or len(inputList) < min:
            print("Please enter the required number of words.")
        else:
            print(inputList)
            break
            
GetWordsFromUser(1, 4)