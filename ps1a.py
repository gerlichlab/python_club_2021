current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * float(input("Enter the portion of salary you are able to save:"))
total_cost = float(input("Enter the cost of your dream house:"))
portion_down_payment = 0.25 * total_cost

i = 0
while current_savings < portion_down_payment:
    current_savings = (current_savings*(1+(r/12))) + portion_saved
    i = i + 1
print("You can move in in",i,"months.")