# Name:
# Date:
# Period:
# Lab: hangman.py
# Description: A simulation of the game hangman.
import random


# get_secret_word DO NOT EDIT
def get_secret_word():
    file = open("word_list.txt", "r+")
    word_bank = file.read().split("\n")
    index = random.randint(0, len(word_bank) - 1)
    return word_bank[index]


# Any helper functions go here


# This is the main game
def main():
    secret_word = get_secret_word()
    print(secret_word)  # Note: Note this line will be removed later. It is here now for debugging purposes.

    # Your code for the game goes here


if __name__ == "__main__":
    main()
