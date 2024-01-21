# This program is by Yoyo Liu
# Complete in 2022 
# Uploaded to Github 1/21/2024

from random import randint
list_of_secret_word = ['algorithm', 'program', 'API', 'argument', 'ASCII', 'boolean', 'bug', 'char', 'object', 'class', 'code', 'function', 'data', 'loop', 'iteration', 'operator', 'variable', 'syntax']

secret_word = list_of_secret_word[randint(0, len(list_of_secret_word))]
missed_letters = ''
correct_letters = ''
game_is_done = False

print("This Hangman is about computer programming! Think hard about CS vocabularies! Good luck!")

hangman_pics = ['''
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
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']


def display_board (missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range (len(secret_word)):
        # replaces blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks [:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        #show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # returns the letter the player entered. This function makes sure the player entered a single letter and not somehting else
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess)!=1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    # This functions returns True if the players wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    display_board(missed_letters, correct_letters, secret_word)
    # Let the player enter a letter
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        #Check if the player has won
        found_all_letters = True
        for i in range (len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! The secret word is ' + secret_word + ''"! You have won!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # CHeck if the player has guessed too many times and lost
        if len(missed_letters) == len(hangman_pics) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' +
                str(len(missed_letters)) + ' missed guesses and ' +
                str(len(correct_letters))+ ' correct guesses, the word was "' + secret_word +'"')
            game_is_done = True

    if game_is_done:
        if play_again():
            secret_word = list_of_secret_word[randint(0, len(list_of_secret_word))]
            print("This Hangman is still about computer programming! Think hard about CS vocabularies! Good luck!")
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
        else:
            break