#Modify ps1a to include the following:
#   1.Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
#   2.After the 6 th month, increase your salary by that percentage. Do the same after the 12th month, the 18th month, and so on.

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

current_savings = 0
r = 0.04
annual_salary = positive_float_input_w_safety_net("Enter your annual salary: ")
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * positive_float_input_w_safety_net("Enter the percent of your salary to save, as a decimal: ")
total_cost = positive_float_input_w_safety_net("Enter the cost of your dream home: ")
portion_down_payment = 0.25 * total_cost
semi_annual_raise = positive_float_input_w_safety_net("Enter the semi-annual raise, as a decimal: ")

i = 0
while current_savings < portion_down_payment:
    current_savings = (current_savings*(1+(r/12))) + portion_saved
    i = i + 1
    if i%6 == 0:
        annual_salary = annual_salary * (1+semi_annual_raise)
        monthly_salary = monthly_salary * (1+semi_annual_raise)
        portion_saved = portion_saved * (1+semi_annual_raise)
print("You can move in in",i,"months.")