# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) # Removed extra equal sign, added bracket, and matched quotation mark

if year <= 1900: # added colon at the end
    print ("Woah, that's the past!") # changed quotation marks to be consistent with the rest of the code
elif year > 1900 and year < 2020: # changed && to 'and'
    print ("That's totally the present!")
else: # changed to else as it is the last statement in the block and does not have a condition
    print("Far out, that's the future!!")