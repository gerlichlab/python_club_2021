#Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats.

def float_input_with_safety_net(prompt):
    """
    This function checks whether the user has provided a valid number as input, and will try again if parameters are not met.
    """
    errormsg = "That number is not valid, please try again"
    while True:
        try: x = float(input(prompt))
        except ValueError:
            print(errormsg)
            x = float_input_with_safety_net(prompt)
        break
    if x <= 0:
        print(errormsg)
        x = float_input_with_safety_net(prompt)
    return x

current_savings = 0
r = 0.04
annual_salary = float_input_with_safety_net("Enter your annual salary: ")
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * float_input_with_safety_net("Enter the percent of your salary to save, as a decimal: ")
total_cost = float_input_with_safety_net("Enter the cost of your dream home: ")
portion_down_payment = 0.25 * total_cost

i = 0
while current_savings < portion_down_payment:
    current_savings = (current_savings*(1+(r/12))) + portion_saved
    i = i + 1
print("You can move in in",i,"months.")