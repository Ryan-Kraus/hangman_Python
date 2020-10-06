# Hangman game:
# This game loads a dictionary file defined in constants, and selects a word at random.
# The dictionary file must be in the same directory as the game file.
# The player has a specified number of incorrect guesses they can make defined in constants.
# The player tries to guess the word through single letters. If the player guesses the word correctly,
# they win the game. If the max number of guesses are reached, the player loses.
# Player guess inputs are limited to single letters, upper or lowercase.
# Players may type <help> to access a help menu, or <quit> to quit the current game.

import random
import string

#------------CONSTANTS-----------#
DICTIONARY = "dictionary.txt"
# File to load secretWord options from

MAX_LIVES = 6
# Number of incorrect guesses the player can make


#------------FUNCTIONS------------#
def loadWords():
    """
    Returns a list of valid words from file in constant DICTIONARY
    Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(DICTIONARY, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    Returns a word from wordlist at random
    wordlist is a list of lowercase words
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """
    returns a boolean: True if all letters of secretWord are in lettersGuessed, else False
    secretWord is a string of the word the user is trying to guess
    lettersGuessed is a list of letters that have been guessed thus far
    """
    i = 0
    while i < len(secretWord):
        if secretWord[i] in lettersGuessed:
            i += 1
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    returns a string, comprised of letters and underscores.
    A letter represents a correctly guessed letter, an underscore represents
    a letter that has yet to be guessed.
    secretWord is a string of the word the user is trying to guess.
    lettersGuessed is a list of what letters have been guessed thus far
    """
    i = 0
    guessedWord = ""
    while i < len(secretWord):
        if secretWord[i] in lettersGuessed:
            guessedWord += secretWord[i]
        else:
            guessedWord += " _"
        i += 1
    return(guessedWord)



def getAvailableLetters(lettersGuessed):
    """
    Prints a list of letters that have not yet been guessed.
    Returns nothing.
    lettersGuessed is a list of what letters have been guessed thus far
    """
    i = 0
    availableLetters = list(string.ascii_lowercase)
    while i < len(lettersGuessed):
        if lettersGuessed[i] in availableLetters:
            availableLetters.remove(lettersGuessed[i])
        i += 1
    print(availableLetters)
    return()


def checkValidInput(guess):
    """
    Checks the user input to make sure it is valid. Valid inputs are lowercase
    letters. Numbers, symbols, and uppercase letters are invalid.
    guess is a string of the modified user input
    returns True if the input is valid, False if the input is not.
    """
    if len(guess) > 1:
        print("please only enter one letter")
        return False
    elif guess in string.ascii_lowercase:
        return True
    else:
        print("This is not a valid input")
        return False


def hangman():
    """
    Begins a game of Hangman
    """

    #Initializations
    #secretWord: string, the secret word to guess
    secretWord = chooseWord(wordlist).lower()

    guessesLeft = MAX_LIVES
    gameOver = False
    lettersGuessed = []

    print('For help, type "help"')

# Initialize the guessedWord to empty spaces for start of game.
    guessedWord = getGuessedWord(secretWord, lettersGuessed)

#game loop
    while (gameOver == False):
        #Set game stage and receive input
        print(guessedWord)
        print("you have " + str(guessesLeft) + " guesses left.")
        getAvailableLetters(lettersGuessed)
        guess = input("Please guess a letter: ")
        guess = guess.lower()

        #Continue game based on input
        #Help Dialogue
        if guess == "help":
            print('The purpose of this game is to guess the secret word.')
            print('You can make up to ' + str(MAX_LIVES) + ' incorrect guesses.')
            print('If you can guess the word without running out of guesses, you win!')
            print(' ')
            print('You can guess any letter. Your guess is not case sensitive.')
            print('Numbers and symbols are not valid inputs. You may only guess one letter at a time.')
            print(' ')
            print('To quit this game, type "quit"')

        #Quit out of the game
        elif guess == "quit":
            break

        #Continue playing the game if the input is valid.
        elif checkValidInput(guess):
            #Check for duplicate guess
            if guess in lettersGuessed:
                print("You have already guessed that letter.")
            else:
                lettersGuessed += guess
                #If Correct guess
                if guess in secretWord:
                    print("Good guess:")
                #If Incorrect guess
                else:
                    guessesLeft -= 1
                    print("Oops! That letter is not in my word.")

                #Set new guessedWord state from most recent user input.
                guessedWord = getGuessedWord(secretWord, lettersGuessed)

                #Game over conditions and actions
                gameOver = isWordGuessed(secretWord, lettersGuessed) or guessesLeft == 0
                if gameOver:
                    if isWordGuessed(secretWord, lettersGuessed):
                        print(secretWord.upper())
                        print("YOU WIN!")
                    elif guessesLeft == 0:
                        print("You Lose.")
                        print("The correct word was: " + secretWord)

#Load dictionary for gameplay
wordlist = loadWords()
#call to start game
hangman()
