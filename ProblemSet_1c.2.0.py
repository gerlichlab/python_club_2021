# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:10:08 2021

@author: emoke.gerocz
"""

starting_salary=float(input('Please enter your starting annual salary!'))

dreamhome_price =1000000
down_payment = dreamhome_price * 0.25
annual_return =0.04
semi_annual_raise =0.07
semi_annual_increase =1 + semi_annual_raise 
months= 36 

portion_saved= 0
min_rate=0
max_rate =10000
epsilon= 100

current_savings = 0
i=0
x=0
steps=1
rate_found= False 

portion_saved=(min_rate+max_rate)/2

while abs(current_savings-down_payment) > epsilon:
    annual_salary=starting_salary
    current_savings = 0
    monthly_return =current_savings * annual_return/12
    steps = steps +1
    
    for i in range(36):
        if x < 5:
            monthly_salary = (annual_salary/12) * (portion_saved/1000)
            current_savings = current_savings + monthly_salary +monthly_return
            x= x+1
            
        else:
            monthly_salary = (annual_salary/12)  * (portion_saved/1000)
            current_savings = current_savings + monthly_salary +monthly_return
            annual_salary = annual_salary * semi_annual_increase
            x=0
    print(current_savings)
    
    if abs(current_savings-down_payment) > epsilon:
        rate_found = True
        break
    
    if current_savings < down_payment - epsilon :
        min_rate = portion_saved
        
    elif current_savings > down_payment - epsilon :
        max_rate =portion_saved
        
    portion_saved=(min_rate+max_rate)/2
    
if rate_found == True:
   print('Success!')
   print('Best savings rate:', portion_saved/10000)
   print ('Steps in bisection search', steps)
else: 
    print ('It is not possible to pay the down payment in 3 years! ')
        
        
            
            