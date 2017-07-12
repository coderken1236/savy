# Name:
# Date:



# proj 03: Guessing Game

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. Keep the game going until the user types exit.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
loop_control = True
random_number = random.randint(1,20)
print "I am guessing a number between 1 and 20. Can you guess my number?"
while loop_control == True:
    guess = raw_input("Enter a number, or 'exit' to end the game: ")
    if guess == 'exit':
        loop_control = False
    elif int(guess) > int(random_number):
        print "Your number is too high"
    elif int(guess) < int(random_number):
        print "Your number is too low"
    elif int(guess) == int(random_number):
        print "Great! You guessed the number"
        loop_control = False






