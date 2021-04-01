r = 0.04
semi_annual_raise = float(0.07)
annual_salary = float(input("Enter your annual salary:"))
monthly_salary = annual_salary / 12
current_savings = 0

low = 0
high = current_savings
guess = (low + high)/2
i = 0
#   I want to do something like:
#   while abs(the total savings after 36 rounds of the function from 1b, with "guess" as the proportion saved variable - (1000000*0.25)) >= 100:
#        if (the total savings after 36 rounds of the function from 1b, with "guess" as the proportion saved variable) < (1000000*0.25):
#            low = guess
#        else:
#           high = guess
#        guess = (high + low)/2.0
#   i = i + 1
#   print("Best savings rate:", guess)
#   print("Steps in bisection search:", i)