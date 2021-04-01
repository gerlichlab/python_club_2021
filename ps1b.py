current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * float(input("Enter the portion of salary you are able to save:"))
total_cost = float(input("Enter the cost of your dream house:"))
portion_down_payment = 0.25 * total_cost
semi_annual_raise = float(input("Enter the proportion raise:"))

i = 0
while current_savings < portion_down_payment:
    current_savings = (current_savings*(1+(r/12))) + portion_saved
    i = i + 1
    if i%6 is 0:
        annual_salary = annual_salary * (1+semi_annual_raise)
        monthly_salary = monthly_salary * (1+semi_annual_raise)
        portion_saved = portion_saved * (1+semi_annual_raise)
print("You can move in in",i,"months.")