#guess number
import random

target = random.randint(1,100)

while True:
    userChoice = input("guess the target or quit(Q):")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)

    if(userChoice == target):
        print("Success: Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number is too small. Take a bigger guess..")
    else:
        print("your number is too big. Take a smaller guess..")

print("--GAME OVER--")


#word guess game
import random
name = input("enter your name:")
print("Good Luck!", name)

words = ["eren", "sukuna", "mikasa", "naruto", "luffy", "zoro", "sanji", "law", "usopp"]
word = random.choice(words)

print("Guess the characters")

# To store the letters the player has guessed
guesses = ""
turns = 9

while turns > 0:
    failed = 0  # Keep track of letters not yet guessed
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")  # Show underscore for unguessed letters #end in the single line as - - - -
            failed+=1
    print()   #move to the next line after the word dispaly     


# If failed is 0, it means all letters are guessed
    if failed == 0:
            print("you win")
            print("the word is:", word)
            break
    print()

    # Ask the player to guess a letter
    guess= input("guess a character:")
    guesses+=guess   # Add that guess to our list of guessed letters

# If the guessed letter is not in the word
    if guess not in word:
            turns -=1   # Reduce the number of turns
            print('Wrong guess. Try again..')
            print("u have", + turns, "more guesses") 

            if turns == 0:
                print("you lose")   



