import random

# initialize variables
guess_list = []
correct_list = []
incorrect_list = []
guess = ""
shown = ""
words = ["cat", "dog", "kitten", "puppy", "house", "home", "storm", "weather", "public", "domino", "bilingual", "photo", "equality", "examine", "walk", "down", "frog"]
final_answer = ""
chances = 7

# select random word from the list of word
selected = random.choice(words)
# print(selected)

# actively reveal the selected word
def display_selected(selected, guess, shown):
    for letter in selected:
        if guess == letter:
            shown += guess + " "
        elif letter in correct_list:
            shown += letter + " "
        else:
            shown += "_ "
    print("Here is your word: {}({} letters total)".format(shown, len(selected)))
    return shown

# check if the letter is in the word, track the guesses
def check(guess):
    count = 0
    if guess in guess_list:
        print("\nYou have already tried to guess the letter '{}'.".format(guess))
    elif guess in selected:
        correct_list.append(guess)
        guess_list.append(guess)
        count = selected.count(guess)
        print("\nNice guess! The letter '{}' is in the word {} time(s).".format(guess, count))
    else:
        print("\nThe letter '{}' is not in the word.".format(guess))
        incorrect_list.append(guess)
        guess_list.append(guess)
        
while True:
    start = input("\nPress enter/return to start, or enter 'Q' to quit: ")
    print("")
    if start.lower() == 'q':
        break
    
    # interact with the user to guess the selected word
    display_selected(selected, guess, shown)
    while len(incorrect_list) < chances and len(final_answer) != len(selected):
        
        # ask for a letter and cache zero index
        guess = input("Choose a letter ({}/{} strikes): ".format(len(incorrect_list), chances))[0].lower()
        
        # initially verify if isalpha, otherwise check if it is a correct guess
        if not guess.replace(' ', '').isalpha():
            print("\nLetters only please. Try again...\n")
        else:
            check(guess)
            
        # display hidden word to user
        print("Selected letters: " + ", ".join(sorted(guess_list)))
        final_answer = display_selected(selected, guess, shown)
        final_answer = final_answer.replace("_", "").replace(" ", "").strip()
        if len(final_answer) == len(selected):
            print("\nYou nailed it! Nice job, you guessed '{}' in {} tries.".format(selected, len(guess_list)))
            break
            
    else:
        print("\nNice try, Here was the word: '{}'. Let's do this again sometime...".format(selected))