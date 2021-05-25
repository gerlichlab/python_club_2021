#Part B
total_cost= float(input("Enter the cost of your dream home:"))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal:"))
annual_salary= float(input("Enter your annual salary:"))
semi_annual_raise= float(input("Enter semi-annual raise, as a decimal:"))

monthly_salary= annual_salary/12
portion_down_payment= 0.25*total_cost
number_of_months= 0
current_savings=0
while portion_down_payment>current_savings : 
    number_of_months+=1       
    if number_of_months % 6==0:
        monthly_salary= monthly_salary + monthly_salary*semi_annual_raise
    current_savings+= monthly_salary*portion_saved + current_savings*0.04/12
print("Number of months:", number_of_months)
