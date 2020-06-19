# to do list:
# read a text file
# pick a random word from it using random function
# start the game function
# guess the letters if its right count the score 1
# if wrong draw the hangman (hang man = 6 body parts)
# max guess is 6
# draw the won game OR end the
# call the function again to play the game
# ------------------------------------------------------#
import random


# play the game again
def play_again():
    input('Do you want to play again? [Y]es or [N]:')
    return input().lower().startswith('y')


# Get random word from file
def get_random_word():
    secret_word = open("words.txt").read().split()
    return random.choice(secret_word)


def start_game():
    guess_count = 0
    guess_limit = 3
    guessed_word = []
    secret_word = get_random_word()
    print('The word contain', len(secret_word), 'letters', '(', secret_word, ')')
    print('you have', guess_limit, 'tries')
    # Game Logic #
    while guess_count < guess_limit:
        guess = input('Guess the word: ')
        # if the user input the correct full secret word
        if guess == secret_word:
            print('you are right that the word')
            print(secret_word)
            play_again()
            break
        # if the user made the right guess
        elif guess in guessed_word:
            print('try something else')
        elif guess in secret_word:
            print('that letter exist in the word')
            guessed_word.append(guess)
            update = ''
            for letter in secret_word:
                if letter in guessed_word:
                    update += letter
                else:
                    update += '?'
            print(update)
        # if the user made the right guess
        elif guess not in secret_word:
            print('sorry that letter is not part of the word')
            guess_count += 1
            print("you have ", guess_limit - guess_count, 'left.')
    else:
        print('*' * 10)
        print('sorry you failed..')
        play_again()


start_game()
