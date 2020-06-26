"""
- TO DO LIST 23-06-2020:
ADD DRAWINGS AND FIX SOME ISSUES
ADD IF THE USER INPUT WRONG GUESS AGAIN

-TO DO LIST 22-06-2020:
ADD CHECK USER INPUT

-TO DO LIST 20-06-2020:
fix the word list
fix play again
fix comments

-TO DO LIST 19-06-2020:
read a text file
pick a random word from it using random function
start the game function
guess the letters if its right count the score 1
if wrong draw the hangman (hang man = 6 body parts)
max guess is 6
draw the won game OR end the
call the function again to play the game
edit the word list
fixing the random function
adding the game function and working with game logic

-TO DO LIST 18-06-2020:
Planning the project
writing words list
reading the words list in python
"""

import random

# DRAWINGS
sketch = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
   [O   |
        |
        |
       ===''', '''
    +---+
   [O]  |
        |
        |
       ===''', '''
    +---+
   [O]  |
    |   |
        |
       ===''', '''
    +---+
   [O]  |
   /|   |
        |
       ===''', '''
    +---+
   [O]  |
   /|\  |
        |
       ===''', '''
    +---+
   [O]  |
   /|\  |
   /    |
       ===''', '''
    +---+          ||||||    ||||||    ||||    ||||||
   [O]  |          ||  |||   |        ||  ||   ||  |||
   /|\  |          ||  |||   ||||     ||||||   ||  |||
   / \  |          ||  |||   |        ||  ||   ||  |||
       ===         ||||||    ||||||   ||  ||   ||||||
        ''']


# GET A RANDOM WORD FROM FILE
def get_random_word():
    secret_word = open("words.txt").read().split()
    return random.choice(secret_word)


# ASK THE USER TO PLAY THE GAME AGAIN
def play_again():
    question = input('>Do you want to play again? Yes or No : ')
    if question.startswith(('y', 'Y')):
        start_game()
    else:
        print('>THANK YOU FOR PLAYING.')
        print('#' * 10, 'MADE WITH ❤︎ IN BERLIN INTERNATIONAL COLLEGE - JUNE 2020', '#' * 10, )
        print('>Coded by: HASAN MAHMOUD <iam_hyh> EHSAN HASHIMI <covid-19>')
        exit()
        return question


# MAIN GAME
def start_game():
    guess_count = int()
    guessed_letters = []
    secret_word = get_random_word()
    guess_limit = 8

    print('#' * 10, "WE LOVE FOOTBALL, LET'S TEST YOUR KNOWLEDGE???", '#' * 10)
    print('>Try to guess the secret word.')
    print(">The secret word contain", len(secret_word), 'letters.')
    print('>Hint: The secret word could be football team or player name.')
    print('>You have [', guess_limit, '] tries.')
    print('')

    # GAME LOGIC
    while guess_limit > guess_count:
        guess = input('Guess a letter or word: ').lower()

        # CHECK IF USER INPUT ALPHABETS
        if not guess.isalpha():
            print(">I don't understand that letter..!?")
            print('=' * 50)
            continue

        # (1) IF THE USER GUESSED THE WORD
        if guess == secret_word:
            print('>You are right the secret word is [', secret_word, ']')
            print('=' * 50)
            play_again()

        # CHECK USER INPUT
        elif len(guess) > 1:
            print('>Only [1] letter or [full word]')
            print('=' * 50)

        # (2) IF THE USER GUESSED THE LETTER AGAIN
        elif guess in guessed_letters:
            print('>You tried that before, try something else.')
            print('>You tried [', guess_count, '] out of [', guess_limit, "]")
            # SHOW LIST OF GUESSED LETTERS
            print(">Letter's you tried: ", end='')
            print(','.join(guessed_letters))
            print('=' * 50)

        # (3) IF THE USER GUESSED THE RIGHT LETTER
        elif guess in secret_word:
            print('>That letter exist in the word')
            guessed_letters.append(guess)

            # SHOW THE USER INPUT
            update = ''
            for letter in secret_word:
                if letter in guessed_letters:
                    update += letter
                else:
                    update += '_'
            print(update)
            print('=' * 50)

            # (4) IF THE USER GUESSED ALL PARTS OF THE WORD
            if update == secret_word:
                print('>You did it...')
                print('>CONGRATULATIONS')
                print('>the secret word is [', update, ']')
                print('=' * 50)
                play_again()

        # (5) IF THE USER MADE THE WRONG GUESS
        elif guess not in secret_word:
            print('>Sorry that letter is not part of the word')
            guessed_letters.append(guess)
            guess_count += 1
            # DRAW HANGMAN PICTURE
            print(sketch[guess_count])
            print('>You have [', guess_limit - guess_count, '] tries left', 'out of [', guess_limit, ']')
            # SHOW LIST OF GUESSED LETTERS
            print(">Letter's you tried: ", end='')
            print(','.join(guessed_letters))
            print('=' * 50)

    else:
        # (6) IF THE USER DON'T HAVE ANY GUESSES
        print('>...GAME OVER...')
        print('>The secret word is....', '[', secret_word, ']')
        play_again()
        return


start_game()
