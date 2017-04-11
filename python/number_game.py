import random

# limit the number of guesses
# catch when someone submits non-integer
# print "too-" low or high
# let people play again

def main():
    
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    num_guesses = 3
                
    while num_guesses > 0:
        # get a number guess from the player
        try:
            guess = int(input("Guess a number between 1 and 10 ({} guesses): ".format(num_guesses)))
        except ValueError:
            print("Numbers only please. Try again...")
            continue
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}.".format(secret_num))
                break
            elif guess < secret_num:
                print("Too Low!")
            elif guess > secret_num:
                print("Too High!")
        num_guesses -= 1
    
    else:
    # if num_guesses == 0 and status == False:
        print("\nNice try. My number was {}.".format(secret_num))
        
    # determine if the player would like to restart the game
    restart = input("Would you like to play again? Y/n: ").lower()
    if restart != "n".lower():
        print("\nAll right, let's do this...")
        main()
    else:
        print("\nThanks for playing. Let's do this again sometime....")
    
if __name__ == "__main__":
    main()
  