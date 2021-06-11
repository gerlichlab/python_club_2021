starting_salary = float(input(f"Enter the starting salary: "))
semi_annual_rise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25

epsilon = 100
min_rate = 0
max_rate = 10000

portion_saved = (max_rate + min_rate) / 2
steps = 0
rate_found = False

while abs(min_rate - max_rate) > 0.1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, 37):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < epsilon:
            min_rate = max_rate
            rate_found = True
            break
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - epsilon:
        min_rate = portion_saved
    elif current_savings > portion_down_payment + epsilon:
        max_rate = portion_saved

    portion_saved = (max_rate + min_rate) / 2

portion_saved = portion_saved / 10000
if rate_found:
    print(f"Starting salary: {starting_salary}")
    print(f"Best savings rate: {portion_saved:.4f}")
    print(f"Steps in bisection search: {steps}")
else:
    print("Is is not possible to pay the down payment in three years")
