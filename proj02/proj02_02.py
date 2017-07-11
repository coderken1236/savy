# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
# Start at 0 add one
counter = 0
Number = raw_input("How many Fibonacci numbers you want to generate? ")
#loop_control = True
Number = int(Number)
number_before = 0
current_number = 1

while counter <  Number:
    counter = counter + 1
    print "current number = ", current_number
    F = current_number
    number_before = current_number
    current_number = F * Number
