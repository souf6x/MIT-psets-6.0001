"""
In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
your program to include the following
      1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
      2. After the 6th month, increase your salary by that percentage.  Do the same after the 12
         month, the 18  month, and so on. 
Write a program to calculate how many months it will take you save up enough money for a down
payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
        1. The starting annual salary (annual_salary)
        2. The percentage of salary to be saved (portion_saved)
        3. The cost of your dream home (total_cost)
        4. The semi­annual salary raise (semi_annual_raise)

@author: souufi
"""

    #asking user for his  annual salary
annual_salary = int(input("Enter your annual salary: "))

    #asking user for the portion of salary being saved
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

    #asking user for the cost of dream hous
total_cost = int(input("Enter the cost of your dream house: "))


semi_annual_rise = float(input("Enter the semi­annual raise, as a decimal: "))

    #calculate the portion down payment of the dream house
portion_down_payment = total_cost * 0.25

    #calculate the monthly salary of the user
monthly_salary = annual_salary / 12

    #set the current saving 0
current_saving = 0

    #set the annual rate as 0.04
r = 0.04

    #♦calculate the portion saved
portion_saving = portion_saved * monthly_salary

    #set number of months as 0
month = 0

    #keep calculate untill the current saving = or bigger tha the porstion down payment
while current_saving <= portion_down_payment:  
        #adding the current saving to the investment and poryion_saving
    current_saving += (current_saving * r / 12) + portion_saving
        #if month divisible by 6 add to the monthly salary the semi annual rise and calculate the new portion_saving
    if(month % 6 == 0 and month != 0):
        monthly_salary += monthly_salary * semi_annual_rise
        portion_saving = portion_saved * monthly_salary
    
    month += 1
print("Number of months:", month)
