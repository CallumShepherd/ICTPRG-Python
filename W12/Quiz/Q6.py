# Write the function between the START and END tags
# START

def SortWordsAlphabetically(input):
    formattedInput = input.lower().split("-")   # converts to lowercase and splits the string into list elements along the hyphens
    formattedInput.sort()                       # sorts the list alphabetically
    sortedInput = "-".join(formattedInput)      # joins the list elements together with hyphens
    return sortedInput                          # returns the resulting string

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))