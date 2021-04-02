annual_salary = float(input ("Enter your annual salary:"))
annual_return = 0.04
semi_annual_raise = 0.07
total_cost = 1000000

half_year_salary = annual_salary/2
down_payment = total_cost * 0.25 
current_savings = 0 
low = 0 
high = 10000 
num_guess = 0
portion_saved = (low+high)/2


maximum_savings = half_year_salary * (1-(1+semi_annual_raise)**6)/(1-(1+semi_annual_raise)) 

if maximum_savings < down_payment:
    print ("With your salary t is not possible to pay the down payment in three years")    
else: 
    while abs(current_savings - down_payment) >= 100:
        current_savings = half_year_salary * portion_saved/10000 * (1-(1+semi_annual_raise)**6)/(1-(1+semi_annual_raise)) 
          
        if current_savings > down_payment:
            high = portion_saved
        else: 
            low = portion_saved 
        portion_saved = (low+high)/2
        num_guess += 1  

print ("Best savings rate: ", portion_saved/10000)
print ("Steps in bisection search:", num_guess)
