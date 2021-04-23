starting_salary = int(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = int(total_cost * 0.25)

current_savings = 0
epsilon = 100
low = 0
high = 10000
guess_portion_saved = (low + high)//2

months = 0
num_guesses = 0

# improvements: two functions for bisection search and for calculating the savings
# the bisection search should take the 1st function as an input (code from Max Spicer) to make it independnt from the input
# this way the bisection search becomes independent of the input you give to it
# this way code blocks can be used separately and for different things


# solution without including 'down payment not possible in three years'
while abs(portion_down_payment - current_savings) >= epsilon:
    current_savings = 0
    annual_salary = starting_salary
    months = 0
    while months <= 36:
        current_savings += int((current_savings*r/12 + annual_salary/12 * (guess_portion_saved/10000)))
        months += 1
        if months % 6 == 0:
            annual_salary += int(annual_salary * semi_annual_raise)
    if current_savings > portion_down_payment:
        high = guess_portion_saved
    if current_savings < portion_down_payment:
        low = guess_portion_saved
    if current_savings < (portion_down_payment - epsilon) and guess_portion_saved >= 9999:
        print("It is not possible to pay the down payment in three years")
        break
    guess_portion_saved = (low + high)//2
    num_guesses += 1
print(f"Best saving rate: {guess_portion_saved/10000}")
print(f"Steps in bisection search: {num_guesses}")


# solution including 'down payment not possible in three years'
while abs(portion_down_payment - current_savings) >= epsilon:
while abs(portion_down_payment - current_savings) >= epsilon and guess_portion_saved < 9999:
    current_savings = 0
    annual_salary = 300000
    months = 0
    while months <= 36:
        current_savings += int((current_savings*r/12 + annual_salary/12 * (guess_portion_saved/10000)))
        months += 1
        if months % 6 == 0:
            annual_salary += int(annual_salary * semi_annual_raise)
    if current_savings > portion_down_payment:
        high = guess_portion_saved
    if current_savings < portion_down_payment:
        low = guess_portion_saved
    guess_portion_saved = (low + high)//2
    num_guesses += 1
if current_savings < (portion_down_payment - epsilon):
    print("It is not possible to pay the down payment in three years")
else:
    print(f"Best saving rate: {guess_portion_saved/10000}")
    print(f"Steps in bisection search: {num_guesses}")