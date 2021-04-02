annual_salary = float(input ("Enter your annual salary:"))
portion_saved = float (input ("Enter the percent of your salary to save, as a decimal:"))
total_cost = float (input ("Enter the cost of your dream home:"))
semi_annual_raise = float (input ("Enter the semi-annual raise, as a decimal:"))

down_payment = total_cost * 0.25 
monthly_salary = annual_salary/12

current_savings = 0 
months = 0 

while current_savings < down_payment: 
    if months % 6 == 0 and months != 0: 
        monthly_salary += monthly_salary*semi_annual_raise
        current_savings += monthly_salary*portion_saved + current_savings*0.04/12
    else: 
        current_savings += monthly_salary*portion_saved + current_savings*0.04/12
    months += 1
    
    
print ("Number of months:", months)
