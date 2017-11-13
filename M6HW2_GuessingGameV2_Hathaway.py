# CTI-100
# M6HW2 GuessingGame Version 2
# Hathaway, Michael
# 10 Nov 2017 

# This program took almost the whole two weeks for me to write.  Although people
# more experiened could have written it in 30 minutes, I did learn alot.  The reason
# I submitted more than one version of the game is that both versions work, but
# both are vastly different.

import random
import math

# A function was created to input the number. To restrict the range, more
# than one line of code was necessary.  Plus we have to make sure the input
# is an integer instead of a string.  Additionally, if you wanted to change
# the range of numbers it can be done in only one place.
def get_number(input_range):
    
    # This loop will say, "run forever" but since there are conditions to
    # check, it will not run forever. To do this as part of a while statement
    # would be too complicated, so this will check conditions inside the loop.
    while True:
        
        # We will try to catch exceptions and errors.
        try:

            # First we will get the input. If this condition is met correctly,
            # it will pass the input to the next function as 'selection'
            selection = input('\nPlease enter your guess (1 to 100): \n')

            # We insure the selection is an integer.  If it fails, it will raise
            # an exception in which case it will skip to EOFError exception.
            selection = int(selection)
                # in which case it will assign the integer as "selection"
            return selection
            # If the selection is out of range, it will raise a ValueError
            raise ValueError
        # the EOFError can be raised by the function 'input'
        except EOFError:
            print('Error reading input. Try again.\n')
            continue # Using 'continue' will go back to the 'while' statement
        # The ValueError can be raised by the conversion to integer (e.g. letter)
        except ValueError:
            print('Invalid input. Valid range: from 1 to 100.\n')
            continue


# This function will run the game one time.  
def play_game():
    # There are several ways to determine range.  This is one of the many.
    # The reason it is (1, 101) instead of (1, 100) is that it uses the zero
    # based numbering system, so to compensate for the zero, the additional
    # one is required. It is assigned as valid_range so it can be used elsewhere.
    valid_range = range(1, 101)

    # The secret number is generated using the random import.
    secret_number = random.choice(valid_range)
    # This lets the player know the number has been selected.
    print('Secret number selected in the range of 1 to 100\n')
    # A while loop will be used to keep track of the number of guesses and attempts.
    guess = 0
    # This is EXTRA CREDIT to keep track of the number of tries.
    attempts = 0
    # The math module was also imported at the beginning of the program.  This was done
    # so we can calculate log base 2 of 100.
    # Logically, the number 100 would be split in half, and that half halved and so on.
    # This can be done mathematically 6.643865 times.
    max_attempts = math.log2(len(valid_range))
    # The number 6.643865 is not in the valid range because we are not using a floating
    # point value and a fractional attempt is not allowed, so the ceiling is set to the
    # next integer which is 7.  The player gets 7 tries.
    max_attempts = math.ceil(max_attempts)

    # The loop is entered the first time becaue 0 is not in range of 1-100.
    while guess != secret_number:
        # Here we check to see if the max number of tries have been exceeded.
        if attempts >= max_attempts:
            print('Max attempts exceeded! YOU LOSE!\n')
            # The game is done at this point, so an empty return is used to exit
            # the play_game function
            return
        # This will let the player know how many attempts are remaining by subtracting
        # the number of attempts taken so far from max_attempts set above.
        print('Number of attempts remaining remaining: \n' + str(max_attempts - attempts))
        # The function that asks for an input number is used to store the result
        # in the variable named 'guess'
        guess = get_number(valid_range)
        # This increases the number of tries.
        attempts = attempts + 1
        # I chose to start high and work lower.  It could be done from low to high.
        if guess > secret_number:
            print('\nTOO HIGH, try again.\n')
        elif guess < secret_number:
            print('\nTOO LOW, try again.\n')
        else:
            print('Congratulations! You guessed it.')
            print('Your number of attempts was: \n' + str(attempts))
            # There is nothing after this line, so if the correct number has not been
            # guessed, it will return to while. It will try to loop, then break because
            # when the while condition fails, it will return because there is no more
            # code in the function.
        
# This is the main function that will call the play_game() function to run.
def main():
    # The play_game function is called to run
    play_game()
    # If y is pressed, the game will start again.  Anything other than y will exit
    # the program to the prompt.
    while input('Play again? (y for yes): ') == 'y':
        play_game()
        
main()
              
   

