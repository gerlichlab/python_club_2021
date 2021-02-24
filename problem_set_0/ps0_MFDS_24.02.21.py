#Write a program that does the following in order:
#   1. Asks the user to enter a number “x”
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”.
#   4. Prints out the log (base 2) of “x”.

import numpy
while True:
    try:
        x = float(input("Enter number x: "))
        break
    except ValueError:
        print("?! I ASKED FOR A NUMBER!")
while True: 
    try:
        y = float(input("Enter number y: "))
        break
    except ValueError:
        print("?! I ASKED FOR A NUMBER!")
print("x**y =",x**y)
print("log2(x) =",numpy.log2(x))
