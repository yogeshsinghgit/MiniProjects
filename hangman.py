# Instagram @dynamic.coding
# Hangman Game in Python
# 
import random

# Here the user is asked to enter the name first
name = input("Enter your name: ")
print("All the best", name)

words = ["website","hangman","rainbow","computer","science",
    "programming","python","mathematics","player"]
# Function will choose one random
# word from this list of words
word = random.choice(words)
print("\nGuess the characters")
guesses = ""
turns = 10 # Number of turns
while turns > 0:
    failed = 0 # counts the number of times a user fails
    # all characters from the input word taking one at a time.
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            # for every failure 1 will be
            # incremented in failure
            failed += 1
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("\n\nYou Win")
        # this print the correct word
        print("\nThe word is: ", word)
        break
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("\n\nguess the character: ")
    # every input character will be stored in guesses
    guesses += guess
    # check input with the character in word
    if guess not in word:
        turns -= 1
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("\nWrong")
        # this will print the number of
        # turns left for the user
        print("\nYou have", +turns, "more guesses")
        if turns == 0:
            print("\n\nYou lose")
