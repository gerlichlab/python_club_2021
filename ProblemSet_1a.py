# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:20:33 2021

@author: emoke.gerocz
"""

""" Problem 1A"""
    

annual_salary=float(input("Please enter your annual salary!"))
total_cost = float(input("What is the cost of your dream home?"))   
portion_saved = float(input("Please enter how much of your salary are you going to save! [Use a decimal point]"))

portion_down_payment= 0.25
price = total_cost * portion_down_payment

r = 0.04
current_savings = 0
annual_return = current_savings*r /12

monthly_salary = (annual_salary/12) * portion_saved
number_of_months= 0

while price > current_savings:
    number_of_months = number_of_months + 1
    current_savings= current_savings + monthly_salary 
    annual_return = current_savings*r /12
    current_savings=current_savings+annual_return
print("Congratulations! You can buy a house now!")
print("Number of months:", number_of_months)




