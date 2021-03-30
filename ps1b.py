#!/usr/bin/env python
# coding: utf-8

# Modify your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6 th month, increase your salary by that percentage. Do the same after the 12
# th th
# month, the 18 month, and so on.
# Write a program to calculate how many months it will take you save up enough money for a down
# payment. LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semiannual
# salary raise (semi_annual_raise)

# In[11]:


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

    
while True:
    try:
        semi_annual_raise = float(input('Input an annual salary increase, paid every six months, as a decimal: '))
    except ValueError:
        print("That's not a number")
    break

#semi_annual_raise paid every 6 months

    
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary/12
current_savings = 0
number_of_months = 0
rate = (current_savings * 0.04)/12


while current_savings < portion_down_payment:
    current_savings += (annual_salary/12)*portion_saved
    current_savings += rate
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Final nnual salary after semi annual raise : ", annual_salary)
print("Percentage of your salary to save each month: ", portion_saved)
print("Total cost of your dream house: ", total_cost)
print("Semi annual raise: ", semi_annual_raise)
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




