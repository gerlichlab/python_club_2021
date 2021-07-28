# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:36:18 2021

@author: emoke.gerocz
"""

""" Problem 1B """


annual_salary=float(input("Please enter your starting annual salary!"))
portion_saved = float(input("Enter the percent of your salary to save as a decimal!"))
total_cost = float(input("Enter the cost of your dream home!"))   
semi_annual_raise_increase = float(input("Enter your semi annual raise, as a decimal!"))

semi_annual_raise= float(1 + semi_annual_raise_increase)

portion_down_payment= 0.25
price = total_cost * portion_down_payment

r = 0.04
current_savings = 0


monthly_salary = (annual_salary/12) * portion_saved
number_of_months= 0

i= 0
   
while price > current_savings:
    if i <= 5:
        number_of_months = number_of_months + 1
        annual_return = current_savings*r /12
        current_savings = current_savings + monthly_salary + annual_return
        i = i + 1
    
    else:
        annual_salary= annual_salary * semi_annual_raise
        monthly_salary = (annual_salary/12) * portion_saved
        i = 0
    
print("Congratulations! You can buy a house now!")
print("Number of months:", number_of_months)
    