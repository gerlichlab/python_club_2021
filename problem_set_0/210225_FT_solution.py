import numpy as np

print(
    "This program calculates the result of raising a number X to the power of Y and the log (base 2) of X"
)
# Input number X
x = float(input("Please input number X: "))
# Input number Y
y = float(input("Please input number Y: "))
# Print out number X raised to the power of Y
print("The results of ", x, " to the power of ", y, " is ", x ** y)
# Print out log (base2) of X if X => 0
if x > 0:
    print("The log2 of ", x, " is ", np.log2(x))
else:
    print("The log of X <= 0 is undefined!")
