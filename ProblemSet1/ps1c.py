#Part C
#semi-annual raise 0.07 (7%)
#annual return of investments 0.04
#downpayment is 25% of 1M house--> 250000
#total time 36 months
#savings within 100$ of downpayment

annual_salary= float(input("Enter your annual salary:"))
semi_annual_raise= 0.07
downpayment=250000
counter=1
high=10000
low=0
portion_saved=((high+low)/2)/10000
current_savings=0
number_of_months=0
monthly_salary= annual_salary/12

def savings_with_current_portion_saved (number_of_months, monthly_salary, current_savings):
    ##this function should determine how much money you will have after 36 months with any given rate of saving
    while number_of_months < 37:  
        number_of_months=+1
        if number_of_months % 6==0:
            monthly_salary= monthly_salary + monthly_salary*semi_annual_raise
        current_savings+= monthly_salary*portion_saved + current_savings*0.04/12
    return (current_savings)
    print(current_savings)
    
if downpayment-current_savings<100 and downpayment-current_savings>0:
    print("Best savings rate is", portion_saved)
    print("Number of guesses 1")
    
elif downpayment-current_savings>100:
    while downpayment-current_savings>100:
        low=(low+high)/2
        portion_saved=((high+low)/2)/10000
        savings_with_current_portion_saved (number_of_months, monthly_salary, current_savings)
        counter=+1
        if high-low<0.001:
            print("You don't earn enough for this house")
        break
    print("Number of guesses", counter)
    print("Best savings rate is", portion_saved)
    
elif downpayment-current_savings<0:
    while downpayment-current_savings<0:
        high=(low+high)/2
        portion_saved=((high+low)/2)/10000
        savings_with_current_portion_saved (number_of_months, monthly_salary, current_savings)
        counter=+1
        if high-low<0.001:
            print("You don't earn enough for this house")
        break
    print("Number of guesses", counter)
    print("Best savings rate is", portion_saved)
