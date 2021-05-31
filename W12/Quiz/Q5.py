# Write the function between the START and END tags
# START

def IsPalindrome(input):
    formattedInput = input.lower().replace(' ', '')
    if formattedInput == formattedInput[::-1]:
        return True
    else:
        return False

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))