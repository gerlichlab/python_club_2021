#!/usr/bin/env python
# coding: utf-8

# At the end of each month, your savings will be increased by the return on your investment,
# plus a percentage of your monthly salary (annual salary / 12).
# 
# Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 1
# Your program should ask the user to enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The portion of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)

# In[108]:


while True:
    try: annual_salary = float(input('Enter your annual salary: '))
    except ValueError:
        print("That's not a number, silly")
    if annual_salary <0:
            print("How can you buy a house if you don't earn any money?")
    break
    
while True:
    try:
        portion_saved = float(input('Enter a percent of your salary to save, as a decimal: '))
    except ValueError:
        print("That's not a number")
    if portion_saved >0 and portion_saved <= 1:
        break
    else:
        print('You must enter the percentage as a decimal between 0 and 1')
        
while True:
    try:
        total_cost = float(input('What is the cost of your dream home?: '))
    except ValueError:
        print("That's not a number")
    if total_cost <0:
            print("Free house? Lucky you")
    break
    
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary/12
current_savings = 0
number_of_months = 0
rate = (current_savings * 0.04)/12

while current_savings < portion_down_payment:
    current_savings += (annual_salary/12)*portion_saved
    current_savings += rate
    number_of_months += 1

print("Annual_salary: ", annual_salary)
print("Percentage of your salary to save each month: ", portion_saved)
print("Total_cost of your dream house: ", total_cost)
print("Number of months to buy your dream house: ", number_of_months)    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




