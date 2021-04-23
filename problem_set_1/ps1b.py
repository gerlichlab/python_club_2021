annual_salary = int(input("Enter your starting annual salary:"))
portion_saved = float(input("Enter the portion of your salary to save, as decimal: ")) # Include error if the value is not given betweeb 0 and 1
total_cost = int(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal:"))

portion_down_payment = total_cost * 0.25 # this is the value you need to reach

current_savings = 0
r = 0.04
months = 0

guess = 0
increment = 1

while portion_down_payment > current_savings:
    current_savings += (current_savings*r/12 + annual_salary/12 * portion_saved)
    guess += increment
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print(f"Number of months:{months}")
