# Write the function between the START and END tags
# START

def FibonacciAdder(n):
    result = 0  # final result
    num0 = 0    # first number in sequence
    num1 = 1    # second number in sequence
    num2 = 0    # next number in sequence (plaeholder) - when loop is complete num3 = result
    for x in range(1, n):
        num2 = num0 + num1
        num0 = num1
        num1 = num2
        result += num0
    return result

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))