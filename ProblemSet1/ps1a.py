#cost of dream home total_cost
#portion of the cost for downpayment portion_down_payment. portion downpayment is 0.25.
#amount saved thus far current_savings
#at the end of month you receive additional current_savings*r/12. r=0.04
#assume annual salary annual_salary
#portion saved is what you put aside yourself portion_saved
#monthly salary is annual_salary/12


#Part A
total_cost= float(input("Enter the cost of your dream home:"))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal:"))
annual_salary= float(input("Enter your annual salary:"))

monthly_salary= annual_salary/12
portion_down_payment= 0.25*total_cost
number_of_months= 0
current_savings=0
while portion_down_payment>current_savings : 
    number_of_months+=1       
    current_savings+= monthly_salary*portion_saved + current_savings*0.04/12
print("Number of months:", number_of_months)
