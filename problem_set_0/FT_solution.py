import numpy as np

print("""
This program calculates the result of raising a number X to the power of Y and the log (base 2) of X
Please input number X
""")
x = int(input ())
print ("Please input number Y")
y = int(input ())
power = pow(x, y)
print ("The results of ", x, " to the power of ", y, " is ",power)
log = (np.log2(x))
print ("The log2 of ", x, " is ", float(log))
