"""
- TO DO LIST 26-06-2020:
ADD MORE GAME ART

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

# ART INSPIRED BY https://www.asciiart.eu/

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
    +---+          ██████╗  ███████╗ █████╗   ██████╗
   [O]  |          ██╔══██╗ ██╔════╝ ██╔══██╗ ██╔══██╗
   /|\  |          ██║  ██║ █████╗   ███████║ ██║  ██║
   / \  |          ██║  ██║ ██╔══╝   ██╔══██║ ██║  ██║
       ===         ██████╔╝ ███████╗ ██║  ██║ ██████╔╝
                   ╚═════╝  ╚══════╝ ╚═╝  ╚═╝ ╚═════╝  
          ''', '''
    ,,,
   (^_^)                                  [o_o]   (^.^) 
 '\_| |_/'                               \_| |_/  \_|_/ 
    | |    Y O U    W O N .  .  .  !       | |      |
   /   \                                  /,  \,   / \   
                                                                                 
        ''']

football = ['''
    -   \O                                   ,      ___
  -     /\                                 O/      |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \, ()  LET'S SCORE A GOAL ..!    ` <<     |   |XX\ 
*************************************************************''', '''
    -   \O                                   ,      ___
  -     /\                                 O/      |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \, ()    LET'S SCORE A GOAL ..!  ` <<     |   |XX\ 
*************************************************************''', '''
    -   \O                                   ,      ___
  -     /\                                 O/      |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \,    -  ()    SCORE A GOAL ..!  ` <<     |   |XX\ 
*************************************************************''', '''
    -   \O                                   ,      ___
  -     /\                                 O/      |   |\ 
 -   __/\ `     -   -   -  () A GOAL ..!   /\      |   |X\ 
    `    \,                               ` <<     |   |XX\ 
*************************************************************''', '''
    -   \O                                   ,      ___
  -     /\    -     -     -   () GOAL ..!  O/      |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \,                               ` <<     |   |XX\ 
*************************************************************''', '''
    -   \O    -     -     -    -  () GOAL  ,  ,     ___
  -     /\                                 |O/     |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \,                              ` <<      |   |XX\ 
*************************************************************''', '''
    -   \O      -     -     -     -   ().. ,  ,     ___
  -     /\                                 |O/     |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \,                              ` <<      |   |XX\ 
*************************************************************''', '''
    -   \O                                 ,O,      ___
  -     /\                                |O/      |   |\ 
 -   __/\ `                                /\      |   |X\ 
    `    \,                               ` <<     |   |XX\ 
*************************************************************''', '''
███╗   ██╗ ██████╗      ██████╗  ██████╗  █████╗ ██╗     
████╗  ██║██╔═══██╗    ██╔════╝ ██╔═══██╗██╔══██╗██║     
██╔██╗ ██║██║   ██║    ██║  ███╗██║   ██║███████║██║     
██║╚██╗██║██║   ██║    ██║   ██║██║   ██║██╔══██║██║     
██║ ╚████║╚██████╔╝    ╚██████╔╝╚██████╔╝██║  ██║███████╗
╚═╝  ╚═══╝ ╚═════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝    ''', '''
 ██████╗      ██████╗      █████╗     ██╗                       ██╗    
██╔════╝     ██╔═══██╗    ██╔══██╗    ██║                       ██║    
██║  ███╗    ██║   ██║    ███████║    ██║                       ██║    
██║   ██║    ██║   ██║    ██╔══██║    ██║                       ╚═╝    
╚██████╔╝    ╚██████╔╝    ██║  ██║    ███████╗    ██╗    ██╗    ██╗    
 ╚═════╝      ╚═════╝     ╚═╝  ╚═╝    ╚══════╝    ╚═╝    ╚═╝    ╚═╝    
          ''']

pacman = ['''
_______________________ P A C - M A N _______________________
 ,---.                                                  ,--.  
/  _.-'     .-.        .-.        .-.         .-.      |oo  |
\  '._.     '-'        '-'        '-'         '-'      |~~  | 
 '---'     DON'T  LET  THEM  EAT  ME . . !             |/\/\|
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.                                                  ,--.  
/  _.-'     .-.        .-.        .-.         .-.      |oo  |
\  '._.     '-'        '-'        '-'         '-'      |~~  | 
 '---'    D O N ' T  L E T  T H E M  E A T  M E . . !  |/\/\|
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.                                             ,--.  
/  _.-'     .-.        .-.        .-.             |oo  |
\  '._.     '-'        '-'        '-'             |~~  | 
 '---'    D O N ' T  L E T  T H E M  E A T  M E . |/\/\|
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.                                      ,--.         .-.
/  _.-'     .-.        .-.        .-.      |oo  |       |OO |
\  '._.     '-'        '-'        '-'      |~~  |       |   |
 '---'    D O N ' T  L E T  T H E  M  E A T|/\/\|       '^^^'
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.                                  ,--.     .-.     .-.
/  _.-'     .-.        .-.        .-.  |oo  |   |OO |   |OO |
\  '._.     '-'        '-'        '-'  |~~  |   |   |   |   |
 '---'    D O N ' T  L E T  T H E  M E |/\/\|   '^^^'   '^^^'
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.                         ,--.     .-.     .-.      .-.
/  _.-'     .-.        .-.    |oo  |   |OO |   |OO |    |OO |
\  '._.     '-'        '-'    |~~  |   |   |   |   |    |   |
 '---'    D O N ' T  L E T  T |/\/\|   '^^^'   '^^^'    '^^^'
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
 ,---.              ,--.        .-.        .-.       .-. 
/  _.-'     .-.    |oo  |      |OO |      |OO |     |OO |
\  '._.     '-'    |~~  |      |   |      |   |     |   |
 '---'    D O N ' T|/\/\|      '^^^'      '^^^'     '^^^'
_____________________________________________________________''', '''
_______________________ P A C - M A N _______________________
           ,--.        .-.           .-.          .-. 
          |oo  |      |OO |         |OO |        |OO |
  .'.     |~~  |      |   |         |   |        |   |
 '---'    |/\/\|      '^^^'         '^^^'        '^^^'
_____________________________________________________________''', '''
___________________________ P A C - M A N ________________________________

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝ ''', '''
 _______________________ P A C - M A N ___________________________________

██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗           ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║           ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║           ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║           ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║    ██╗    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝    ╚═╝    ╚═╝
__________________________________________________________________________
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
        print('>MADE WITH ❤︎ IN BERLIN INTERNATIONAL COLLEGE - JUNE 2020')
        print('>CODE BY: HASAN MAHMOUD <iam_hyh> EHSAN HASHIMI <covid-19>')
        exit()
        return question


# Global Variable
game_art = ''


# Which game you want to play
def select_art():
    global game_art
    print('>Please select which game art you want to play with?')
    question = input('>[1]: Classic [2]: football : [3]: Pacman : ')
    if question == '1':
        game_art = sketch
        print('>Okay, You are playing classic.')
        print('=' * 63)
    elif question == '2':
        game_art = football
        print(">football, Let's play that.")
        print('=' * 63)
    elif question == '3':
        game_art = pacman
        print('>Pacman, I like that.')
        print('=' * 63)
    else:
        print('Please select 1, 2 OR 3')
        print('=' * 63)
        select_art()
    return game_art


# MAIN GAME
def start_game():
    guess_count = 0
    guessed_letters = []
    secret_word = get_random_word()
    guess_limit = 8

    print('#' * 3, "WE LOVE FOOTBALL, LET'S TEST YOUR KNOWLEDGE???", '#' * 3)
    print('>Try to guess the secret word.')
    print(">The secret word contain", len(secret_word), 'letters.')
    print('>Hint: The secret word could be football team or player name.')
    print('>You have [', guess_limit, '] tries.')
    print('=' * 63)

    # SET GAME ART
    select_art()

    # GAME LOGIC
    while guess_limit > guess_count:
        guess = input('Guess a letter or word: ').lower()

        # CHECK IF USER INPUT ALPHABETS
        if not guess.isalpha():
            print(">I don't understand that letter..!?")
            print('=' * 63)
            continue

        # (1) IF THE USER GUESSED THE WORD
        if guess == secret_word:
            print(game_art[9])
            print('>You are right the secret word is [', secret_word, ']')
            print('=' * 63)
            play_again()

        # CHECK USER INPUT
        elif len(guess) > 1:
            print('>Only [1] letter or [full word]')
            print('=' * 63)

        # (2) IF THE USER GUESSED THE LETTER AGAIN
        elif guess in guessed_letters:
            print('>You tried that before, try something else.')
            print('>You tried [', guess_count, '] out of [', guess_limit, "]")
            # SHOW LIST OF GUESSED LETTERS
            print(">Letter's you tried: ", end='')
            print(','.join(guessed_letters))
            print('=' * 63)

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
            print('=' * 63)

            # (4) IF THE USER GUESSED ALL PARTS OF THE WORD
            if update == secret_word:
                print('>You did it...')
                print('>CONGRATULATIONS')
                print('>the secret word is [', update, ']')
                print(game_art[9])
                print('=' * 63)
                play_again()

        # (5) IF THE USER MADE THE WRONG GUESS
        elif guess not in secret_word:
            guessed_letters.append(guess)
            guess_count += 1

            # DRAW ART
            print(game_art[guess_count])
            print('>Sorry that letter is not part of the word')
            print('>You have [', guess_limit - guess_count, '] tries left', 'out of [', guess_limit, ']')
            # SHOW LIST OF GUESSED LETTERS
            print(">Letter's you tried: ", end='')
            print(','.join(guessed_letters))
            print('=' * 63)

    else:
        # (6) IF THE USER DON'T HAVE ANY GUESSES
        print('>The secret word is....', '[', secret_word, ']')
        print('=' * 63)
        play_again()
        return


start_game()
