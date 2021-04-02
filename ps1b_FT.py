down_payment_percentage = 0.25
annual_return = 0.04
months = 0
current_savings = 0

total_cost = float(input("Please input the cost of your dream house: "))
annual_salary = float(input("Please input your annual salary: "))
portion_saved = float(input(
    "Please input the percentage of your salary you want to save as decimals: "))
semi_annual_raise = float(
    input('Please input your semi-annual raise, as a decimal: '))

monthly_salary = annual_salary/12
monthly_return = annual_return/12
down_payment = down_payment_percentage*total_cost

while current_savings <= down_payment:
    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

print("Annual salary: ", annual_salary)
print("Percentage of the salary to save each month: ", portion_saved)
print("Percentage of the semi annual raise:", semi_annual_raise)
print("Cost of your dream house: ", total_cost)
print("Number of months to wait to buy your dream house: ", months)
