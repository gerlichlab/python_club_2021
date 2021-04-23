annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the portion of your salary to save, as decimal: ")) # Include error if the value is not given betweeb 0 and 1
total_cost = int(input("Enter the cost of your dream home:"))

portion_down_payment = total_cost * 0.25 # this is the value you need to reach

current_savings = 0
r = 0.04
months = 0

guess = 0
increment = 1
epsilon = 0

while portion_down_payment > current_savings:
    current_savings += (current_savings*r/12 + annual_salary/12 * portion_saved)
    guess += increment
    months += 1
print(f"Number of months:{months}")

