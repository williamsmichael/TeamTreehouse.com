import os
import sys
import random

# initialize variables
words = [
    "cat", 
    "dog", 
    "kitten", 
    "puppy", 
    "house", 
    "home", 
    "storm", 
    "weather", 
    "public", 
    "domino", 
    "section", 
    "photo", 
    "equal", 
    "exam", 
    "walk", 
    "down", 
    "frog"
]
chances = 10

# clear the screen for cleaner game experience
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# actively reveal the selected word when the user guesses correctly
def display_selected(selected, guess, guess_list, correct_list, shown):
    clear()
    
    for letter in selected:
        if guess == letter:
            shown += guess + " "
        elif letter in correct_list:
            shown += letter + " "
        else:
            shown += "_ "
    print("\nSelected letters: " + ", ".join(sorted(guess_list)))
    print('')
    print("Here is your word: {}({} letters total)".format(shown, len(selected)))
    print('')
    return shown

# check if the letter is in the word, track hown many instances of the letter in the word
def check(selected, guess, guess_list, correct_list, incorrect_list):
    count = 0
    
    while True:
        # ask for a letter and cache zero index
        guess = input("Choose a letter ({}/{} strikes): ".format(len(incorrect_list), chances))[0].lower()
        
        # initially verify if isalpha, otherwise check if it is a correct guess
        if not guess.replace(' ', '').isalpha():
            print("\nLetters only please. Try again...\n")
        elif guess in guess_list:
            print("\nYou have already tried to guess the letter '{}'.".format(guess))
        else:
            return guess
           
# interact with the user and play the game
def play(done):
    clear()
    guess_list = []
    correct_list = []
    incorrect_list = []
    guess = ""
    shown = ""
    selected = random.choice(words)
    
    while True:
        display_selected(selected, guess, guess_list, correct_list, shown)
        guess = check(selected, guess, guess_list, correct_list, incorrect_list)
        
        if guess in selected:
            correct_list.append(guess)
            guess_list.append(guess)
            count = selected.count(guess)
            found = True
            for letter in selected:
                if letter not in correct_list:
                    found = False
            if found:
                print("\nYou nailed it! Nice job. You guessed '{}' in {} tries.".format(selected, len(guess_list)))
                done = True
        else:
            incorrect_list.append(guess)
            guess_list.append(guess)
            if len(incorrect_list) == chances:
                print("\nNice try, Here was the word: '{}'.".format(selected))
                done = True
                
        if done:
            play_again = input("Play again? Y/n: ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                clear()
                print("\nThanks for playing Letter Guess!\n")
                sys.exit()

# verifies if user wants to continue to the game
def welcome():
    print('\nWelcome to Letter Guess!')
    start = input("\nPress enter/return to start, or enter 'Q' to quit: ")
    if start.lower() == 'q':
        print("ciao!")
        sys.exit()
    else:
        return True
    
# begins the game with intro
done = False
while True:
    clear()
    welcome()
    play(done)