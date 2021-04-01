#I tried but couldn't manage to make it work, I think it enters an endless loop somewhere snce I don't have any breaks if the salary is too low

#Part C
#semi-annual raise 0.07 (7%)
#annual return of investments 0.04
#downpayment is 25% of 1M house--> 250000
#total time 36 months
#savings within 100$ of downpayment

annual_salary= float(input("Enter your annual salary:"))
semi_annual_raise= 0.07
downpayment=250000
monthly_salary= annual_salary/12
counter=1
number_of_months=0
high=10000
low=0
portion_saved=((high+low)/2)/10000
while number_of_months < 37:  
    number_of_months=+1
    if number_of_months % 6==0:
        monthly_salary= monthly_salary + monthly_salary*semi_annual_raise
    current_savings+= monthly_salary*portion_saved + current_savings*0.04/12

if downpayment-current_savings<100 and downpayment-current_savings>0:
    print("Best savings rate is", portion_saved)
    print("Number of guesses 1")
    
elif downpayment-current_savings>100:
    while downpayment-current_savings>100:
        low=(low+high)/2
        portion_saved=((high+low)/2)/10000
        while number_of_months<37:  
            number_of_months=+1
            if number_of_months % 6==0:
                 monthly_salary= monthly_salary + monthly_salary*semi_annual_raise
            current_savings+= monthly_salary*portion_saved + current_savings*0.04/12
        counter=+1
    print("Number of guesses", counter)
    
elif downpayment-current_savings<0:
    while downpayment-current_savings<0:
        high=(low+high)/2
        portion_saved=((high+low)/2)/10000
        while number_of_months<37:   
            number_of_months=+1
            if number_of_months % 6==0:
                monthly_salary= monthly_salary + monthly_salary*semi_annual_raise
            current_savings+= monthly_salary*portion_saved + current_savings*0.04/12
        counter=+1
    print("Number of guesses", counter)
