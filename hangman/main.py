import art

from replit import clear
from brain import Hangman

# import and define hangman class
hangman = Hangman()
hangman.change_word()


# function display all commands available
def menu():
    print(f'Computer has selected {hangman.capacity()} length word\n')
    print('Type "-q" to quit the game.')
    print('Type "-c" to change the word.')
    print('Type "-s" to start the game.')


# function to start the game
def start():
    print(art.welcome)
    print(art.logo)
    menu()
    quit_the_game = False

    # check user wants to quit the game
    while not quit_the_game:
        user_input = input('>')
        if user_input == '-c':
            hangman.change_word()
            menu()
        elif user_input == '-q':
            quit_the_game = True
        elif user_input == '-s':
            game()
        else:
            print('You entered a wrong input. Enter a valid input')
            clear()
            menu()


# function to control the game
def game():
    end_the_game = False

    # check is game ene or not
    while not end_the_game:
        guess = input("Guess a letter: ").lower()

        # when user guess already guessed
        if hangman.is_guess_in_display(guess):
            print(f'You\'ve already guessed {guess}')
        else:
            hangman.position(guess)

            if not hangman.is_guess_in_word(guess):
                print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
                hangman.minus_life()

                if hangman.is_lives_empty():
                    end_the_game = True
                    print('You lose.')

                print(f"{' '.join(hangman.get_display())}")

                if hangman.is_win():
                    print('You win.')
                    end_the_game = True

        print(hangman.lives_art())


if __name__ == '__main__':
    start()
