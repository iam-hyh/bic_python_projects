# TO DO LIST 20-june-2020:
# fix the word list
# fix play again
# add drawings
# fix comments
#
# TO DO LIST 19/06/2020
# read a text file
# pick a random word from it using random function
# start the game function
# guess the letters if its right count the score 1
# if wrong draw the hangman (hang man = 6 body parts)
# max guess is 6
# draw the won game OR end the
# call the function again to play the game
# edit the word list
# fixing the random function
# adding the game function and working with game logic
#
# TO DO LIST 18/06/2020
# Planning the project
# words list
# reading the words list in python
# ------------------------------------------------------#
import random


# GET A RANDOM WORD FROM FILE
def get_random_word():
    secret_word = open("words.txt").readline().split()
    return random.choice(secret_word)


# ASK THE USER TO PLAY THE GAME AGAIN
def play_again():
    answer = input('Do you want to play again? [Y]es or [N]:')
    if answer == 'y' or answer == 'yes':
        start_game()
    elif answer == 'n' or answer == 'no':
        print('Thank you for playing.')
        print('#' * 10, 'MADE WITH ❤︎ IN BERLIN INTERNATIONAL COLLEGE', '#' * 10, )
        print(' ' * 15, 'Dev Team: HASAN MAHMOUD <iam_hyh> Ehsan <covid-19>')
    else:
        print('invalid input.')
        play_again()


# MAIN GAME
def start_game():
    guess_count = 0
    guess_limit = 1
    guessed_word = []
    secret_word = get_random_word()
    print('#' * 10, 'WE LOVE FOOTBALL, LET\'S TEST YOUR KNOWLEDGE???', '#' * 10)
    print('The word contain', len(secret_word), 'letters', '(', secret_word, ')',)
    print('you have', guess_limit, 'tries')
    # GAME LOGIC #
    while guess_count < guess_limit:
        guess = input('Guess the word: ')
        # (1) IF THE USER GUESSED THE WORD
        if guess == secret_word:
            print('you are right that the word')
            print(secret_word)
            print('=' * 50)
            play_again()
            break
        # (2) IF THE USER GUESSED THE LETTER AGAIN
        elif guess in guessed_word:
            print('try something else')
            print('=' * 50)
        # (3) IF THE USER GUESSED THE RIGHT LETTER
        elif guess in secret_word:
            print('that letter exist in the word')
            guessed_word.append(guess)
            # SHOW THE USER INPUT
            update = ''
            for letter in secret_word:
                if letter in guessed_word:
                    update += letter
                else:
                    update += '_'
            print(update)
            # (4) IF THE USER GUESSED ALL PARTS OF THE WORD
            if update == secret_word:
                print('you guess it...')
                print('=' * 50)
                play_again()
                print(update)
        # (5) IF THE USER MADE THE WRONG GUESS
        elif guess not in secret_word:
            print('sorry that letter is not part of the word')
            guess_count += 1
            print("you have ", guess_limit - guess_count, 'left.')
            print('=' * 50)
    else:
        # (6) IF THE USER DON'T ANY GUESSES
        print('=' * 50)
        print('sorry you failed..')
        play_again()


start_game()
