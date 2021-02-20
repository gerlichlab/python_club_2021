#Write a program that does the following in order:
#   1. Asks the user to enter a number “x”
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”.
#   4. Prints out the log (base 2) of “x”.

import numpy
x,y = float(input("Enter number x: ")), float(input("Enter number y: "))
print("x**y =",int(x**y))
print("log2(x) =",int(numpy.log2(x)))
