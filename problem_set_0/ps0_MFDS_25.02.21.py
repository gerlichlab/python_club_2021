#The assignment was to write a programme that does the following in order:
#   1. Asks the user to enter a number “x”
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”.
#   4. Prints out the log (base 2) of “x”.
#
#My original solution to this problem was as follows:
# import numpy
# x = float(input("Enter number x: "))
# y = float(input("Enter number y: "))
# print("x**y =",float(x**y)
# print("log2(x) =",float(numpy.log2(x))) 
#
#
#For v2, I wanted the programme to recognise if the user fails to enter a number and, rather than produce a ValueError, ask again for a number with a medium amount of sass:


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
