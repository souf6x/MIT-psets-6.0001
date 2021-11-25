"""
In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a 
program to answer that question.  To simplify things, assume:
          1. Your semi­annual raise is .07 (7%)
          2. Your investments have an annual return of 0.04 (4%)  
          3. The down payment is 0.25 (25%) of the cost of the house 
          4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 
In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).


@author: souufi
"""
    #get the annual salary from the user
annual_salary = int(input("Enter the starting salary: "))

    #constants
semi_annual = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
portion_saving = 0
salary = 0
k = 0
p = 10000

    #check if you can save money for that
if annual_salary <= portion_down_payment / 2:
    print("It is not possible to pay the down payment in three years")
else:
    
    while True:
          #calculate the mid point for bisssection search
        d = int((k + p) / 2)
          #calculate the portion saved
        portion_saved = d  / 10000
          #calculate the monthly salary and the poryion saving
        monthly_salary = annual_salary / 12
        portion_saving = portion_saved * monthly_salary
        current_saving = 0
          #check if this poryion saved good enough
        for i in range(36):  
        
            current_saving += (current_saving * r / 12) + portion_saving
            if(i % 6 == 0 and i != 0):
                monthly_salary += monthly_salary * semi_annual
                portion_saving = portion_saved * monthly_salary   
        if current_saving < portion_down_payment :
            k = d + 1
        elif current_saving - portion_down_payment > 704:
            p = d - 1
        else:
            break
        salary += 1
        
    print("Best saving rate:", portion_saved)
    print("Steps in bisection search:", salary)


    
