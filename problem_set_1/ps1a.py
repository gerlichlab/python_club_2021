annual_salary = float(input ("Enter your annual salary:"))
portion_saved = float (input ("Enter the percent of your salary to save, as a decimal:"))
total_cost = float (input ("Enter the cost of your dream home:"))

down_payment = total_cost * 0.25 
monthly_salary = annual_salary/12

current_savings = 0 
count = 0 
while current_savings < down_payment: 
    current_savings += monthly_salary*portion_saved + current_savings*0.04/12
    count += 1
    
print ("Number of months:", count)
