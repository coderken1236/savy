# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
print "Welcome to Hangman!"
print " I am your host Computer"
print "Let's get started"
random_word = choose_word(wordlist)
list = []
str = random_word
for letter in str:
    list.append(letter)
list1 = []
len(list1)
print len(list)
for letter in list:
    list1.append("_")
print list1
counter1 = 6

while counter1 > 0:
        guess = raw_input("Guess a letter!: ")

        answer = False

        if guess in list:
            print "That letter is in the word."

            counter2 = 0
            while counter2 < len(list):
                if guess == list[counter2]:
                    list1[counter2] = guess
                    answer = True
                counter2 = counter2 + 1
                    #print "That's correct!"

        elif counter1 == 6 and answer == False:
            print "Sorry, that is not one of the letters."
            print "____"
            print "|   O"
            print "|"
            print "|___"
            counter1 = counter1 - 1
            print "you have ", counter1, "guesses left"
        elif counter1 == 5 and answer == False:
            print "Sorry, that is not one of the letters."
            print "____"
            print "|   O"
            print "|   |"
            print "|___"
            counter1 = counter1 - 1
            print "you have ", counter1, "guesses left"
        elif counter1 == 4 and answer == False:
            print "Sorry, that is not one of the letters."
            print"_____"
            print"|    O"
            print"|    |-"
            print"|___"
            counter1 = counter1 - 1
            print "you have ", counter1, "guesses left"
        elif counter1 == 3 and answer == False:
            print "Sorry, that is not one of the letters."
            print"____"
            print"|    O"
            print"|   -|-"
            print"|___"
            counter1 = counter1 - 1
            print "you have ", counter1, "guesses left"
        elif counter1 == 2 and answer == False:
            print "Sorry, that is not one of the letters."
            print"_____"
            print"|    O"
            print"|   -|-"
            print"|___ L"
            counter1 = counter1 - 1
            print "you have ", counter1, "guesses left"
        elif counter1 == 1 and answer == False:
            print "Sorry, that is not one of the letters."
            print"_____"
            print"|    O"
            print"|   -|-"
            print"|___ LL"
            counter1 = counter1 - 1
            print "Sorry you have no more guesses"
            print "The word was", random_word
        print list1