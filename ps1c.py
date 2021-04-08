# Write a program to calculate the best savings rate, as a function of your starting salary.

def positive_float_input_w_safety_net(prompt):
    """
    This function checks whether the user has provided a valid number as input, and will try again if parameters are not met.
    """
    errormsg = "That number is not valid, please try again"
    while True:
        try: x = float(input(prompt))
        except ValueError:
            print(errormsg)
            x = positive_float_input_w_safety_net(prompt)
        break
    if x <= 0:
        print(errormsg)
        x = positive_float_input_w_safety_net(prompt)
    return x

def total_search(guess, annual_salary):
    """
    This function asks for an annual salary as input, and runs a 36-fold loop to calculate a final current_savings value, based on a guess of proportion_saved.
    """
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    portion_saved = monthly_salary * (guess)
    semi_annual_raise = 0.07

    i = 0
    while i < 36:
        current_savings = (current_savings*(1+(r/12))) + portion_saved
        i += 1
        if i%6 == 0:
            annual_salary = annual_salary * (1+semi_annual_raise)
            monthly_salary = monthly_salary * (1+semi_annual_raise)
            portion_saved = portion_saved * (1+semi_annual_raise)
    return current_savings

total_cost = 1e6
portion_down_payment = 0.25 * total_cost
annual_salary = positive_float_input_w_safety_net("Enter your annual salary: ")

low = 0
high = total_search(1, annual_salary)
guess = (low + high)/2
iterations_searched = 0
while abs(total_search(guess, annual_salary) - portion_down_payment) > 100:
    if total_search(guess, annual_salary) < portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    iterations_searched += 1
if guess > 1:
    print("It is not possible to pay down the payment in three years. You would have to save at least", str(guess)[0:6],"times your salary.")
else:
    print("Best savings rate: ", str(guess)[0:6])
    print("Steps in bisection search: ", iterations_searched)