# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

loop_var = True
while loop_var == True:
    x=raw_input('enter any word: ')
    x = str(x)
    lst = []
    for letter in x:
        lst.append(letter)

    lst1 = []
    for letter in x:
        lst1.append(letter)
    lst.reverse()

    if lst == lst1:
        print ('your word is a palindrome')
    else:
        print ('your word is not a palindrome')
    y = raw_input ('would you like to play again? ')
    y = str(y)
    if y == 'no' :
        loop_var = False