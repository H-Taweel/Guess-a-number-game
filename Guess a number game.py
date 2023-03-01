import random

triesLimit = 7  # define triesLimit to use it in the message below
print("Hello! What is your name?")
playerName = input().capitalize()
print(f"Well {playerName}, I am thinking of a number between 0 and 100.\nYou have {triesLimit} tries")

play = True
playCount = 0
while play:
    secret = random.randint(0, 100)
    tries = 0
    guess = ""
    guessesList = []

    while guess != secret:

        guess = input("What is your guess? \n")
        if not guess.isdigit():
            print("\033[91mDoesn't look like a number, this try doesn't count.\033[0m")
        else:
            guess = int(guess)
            tries += 1
            guessesList.append(guess)
            if tries == triesLimit and guess != secret:
                print("Wrong guesses! Better Luck next time")
                print("The secret number was", secret)
                break
            else:
                remainTries = triesLimit - tries
                if guess < secret and guess < (secret - 5):
                    print(f"You need to guess higher. Try again!\nYou still have {remainTries} more guesse(s)")
                elif guess < secret and guess >= (secret - 5):
                    print(
                        f"You're almost there.. you need to guess a BIT HIGHER. Try again!\nYou still have {remainTries} more guesse(s)")
                elif guess > secret and secret < (guess - 5):
                    print(f"You need to guess lower. Try again!\nYou still have {remainTries} more guesse(s)")
                elif guess > secret and secret >= (guess - 5):
                    print(
                        f"You're almost there.. you need to guess a BIT LOWER. Try again!\nYou still have {remainTries} more guesse(s)")

    if guess == secret:
        print(f"Good job, {playerName}! You got it, you found my seceret in {tries} gusse(s)!")
    # tries = 0
    playCount += 1
    print("\033[1;32;47mYou've played " + str(playCount) + " round(s), Your guesses were as follows: ", guessesList,
          "\033[0m")

    answers = ["no", "n", "yes", "y"]
    playAgain = input(playerName + " Would you like to play again? type y or n:\n").lower()
    while playAgain not in answers:
        print('\033[91mPlease type "yes" or "y" to play again    OR\nIf you want to end this game please type "no" or "n"\033[0m')
        playAgain = input().lower()

    if playAgain == "yes" or playAgain == "y":
        play = True
    elif playAgain == "no" or playAgain == "n":
        play = False