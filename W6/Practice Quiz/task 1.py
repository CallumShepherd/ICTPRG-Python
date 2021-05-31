# Imported random module
import random

# Variables
number = random.randrange(1, 25) # random number generator
guess_count = 7 # how many guesses in the game
guess_log = [] # list for storage of guesses

# Starting message
print("\nThe game has begun! Try to guess the correct number between 1 and 25.")

# Loops through each guess in the number of guesses left
for guess in range(guess_count):

    # Gathers input from the user
    guess = int(input("\nEnter your guess: "))

    # First if statement - checks if input is within the right range
    if guess > 0 and guess < 26:

        # Decrements the guess count after each guess made
        guess_count -= 1

        # Adds the number guessed to the list to be printed at the end
        guess_log.append(guess)

        # Checks if winning condition is satisfied
        if guess == number:
            print(f"\nYou have won the game, congratulations!\n\nYour guesses were:\n{guess_log}\n")

            # Stops the program after the game is won
            break

        # If correct number is not guessed, go through this part
        else:
            
            # If there are guesses left to be used in the game, go through this part
            if guess_count > 0:
                if guess > number:
                    print("\nToo high!")
                
                # "elif" used over "else" to make the code more readable
                elif guess < number:
                    print("\nToo low!")
                
                # Tells user how many guesses they have left
                print(f"\nYou have {guess_count} guesses remaining.") 
            
            # Losing condition when user has run out of guesses
            else: 
                print(f"\nYou have lost the game! The correct number was {number}.\n\nYour guesses were:\n{guess_log}\n")
                
                # Stops the program after the game is lost
                break
    
    # Basic input validation that limits the guess between the right range
    else:
        print("\nPlease enter an integer between 1 and 25.")