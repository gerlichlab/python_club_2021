#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

# In[2]:


#Input variables are integers


# In[3]:


x = int(input('Enter a number "x": '))
y = int (input ('Enter a number "y" : '))
print("X**y =", x**y)
print("log2(x) = ", np.log2(x))


# In[4]:


#Catching errors >>> would not work if the input number were negative nor if the input were letters.
#Input should be a float >>> the input should be a float, as if a float were entered then a value error would be raised.
# Writing the code in VSC rather than an ipynb.


# In[32]:


#Input variables are floats


# In[27]:


x = float(input('Enter a number "x": '))
y = float(input ('Enter a number "y" : '))
print("X**y =", x**y)
print("log2(x) = ", np.log2(x))


# In[34]:


#Inputs are integers, output is a string


# In[33]:


x = int(input('Enter a number "x": '))
y = int (input ('Enter a number "y" : '))
print("X**y =", str(x**y))
print("log2(x) = ", str(np.log2(x)))


# In[ ]:





# In[ ]:





# - Comparison of equality of floating point numbers, is a number really the same? np.issame >>> 

# In[ ]:




