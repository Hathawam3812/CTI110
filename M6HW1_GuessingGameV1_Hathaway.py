# CTI-100
# M6HW2 Guessing Game
# Hathaway Michael
# 11 Nov 2017

# This is version 1.  It is not as 'bells and whistles' as version 2.
# I used the most basic commands I could and used the fewest lines of code
# that I could.  That limits its bells and whistles, but it still works.
# I did learn alot from doing this and dissecting the dice and coin games.

# Import the random built-in operation 'random'
import random

# sets the numerical input limits
LOW = 1
HIGH = 100


# This defines the play_game() guessing game
def play_game():
    # Game greeting. /t is tabbed horizontal whitespace
    # to center of text. /n inserts a blank line of whitespace.
    print("\n\tWelcome to 'Guessing Game'!")

    # The '\n' creates a new line, then prints the statement.
    print("\n\nI picked a secret number between 1 and 100.\n")

    # Setting the value range between 1 and 100
    secret_number = random.randint(LOW, HIGH)

    # Ask the user for an integer input, assumed to be between 1 - 100
    # as per the printed statement that states the obvious.
    guess = int(input('Take a guess...'))
    

    # Sets the inital tries value to one 
    tries = 1

    # Game loop
    while guess != secret_number:
        
        if guess > secret_number:
            
            print('Your number was too high... go LOWER.')
            
        else:
            
            print('Your number was too low... go HIGHER.')
            
        # Ask the user for an integer input if the initial try was not the correct number
        guess = int(input('Take a guess...'))

        # Adds the above try to additional tries
        tries += 1

    # Congratulates the user for guessing the correct number.
    print('\nYou got it! The number was: ', secret_number)

    # Displays how many tries it took to guess the correct number.
    print('\nIt took you ', tries, 'tries.')

# This is the main loop that calls the play_game() function.
def main():
    
    # This calls the play_game function
    play_game()
    
    # While the input is 'y', the game fuction will be called again.
    # Otherwise, the game will exit.
    while input('Play again? (y for yes) Any other key to exit: ') == 'y':
        
        play_game()
        
# Calls the main function       
main ()
                
                
