import math
# create a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator
# print out a statement that allows the user to see two calculators that may be chosen
print('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
''')
print(" ")

# request the user to input their selection.
# capitilisation should not effect the program procedure - convert input to lowercase
# print out an error message if there is no valid input
financial_calculator= input("Enter your calculator selection:\t").lower()
print(" ")

# use if-elif-else for the menu selection
# if bond, request the user to input the present value of the house, interest rate, and the amount of months they plan to repay bond within.
# bond repayment formula: x=(i.P)/(1-(1 + i)**(-n))
# ‘P’ is the present value of the house.
# ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
# ‘n’ is the number of months over which the bond will be repaid.
# calculate how much money the user will have to repay each month 
# print out the answer. 
if financial_calculator == "bond":
    house_value= float(input("What is the present value of the house?: \nR"))
    print(" ")
    interest_rate= (float(input("What is the interest rate as a percentage?: \n"))/100 /12)                       
    print(" ")
    repayment_months= float(input("For how many months do you plan to repay the bond?: \n"))
    print(" ")
    monthly_repayment_amount= round((interest_rate * house_value) / (1 - (1 + interest_rate)**(-1 * repayment_months)), 2)
    print(f"The monthly repayment for the bond: R{monthly_repayment_amount} \t")

# elif investment, request the user to input the amount of money that they are depositing,  interest rate (as a percentage; no. only),  & the number of years they plan on investing for
# request the user to input whether they want “simple” or “compound” interest, and store this in a variable called interest.
# capitilisation should not effect the program procedure - convert interest input to lowercase
elif financial_calculator == "investment":
    deposit_amount= float(input("What is the amount of money for the deposit?: R"))
    print(" ")
    interest_rate= float(input("What is the interest rate as a percentage?: "))
    print(" ")
    investment_years= int(input("The number of years planning to invest: "))
    print(" ")
    interest= input("Enter the type of interest to calculate: (simple/compound) \n").lower()
    print(" ")

# use if-elif for the investment interest selection type with 1 tab space as a subsection
# if investment, request the user to input whether they want “simple” or “compound” interest, and store this in a variable called interest.    
# Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate
# simple interest formula: A =P*(1+r*t)
# compound interest formula: A = P* math.pow((1+r),t)
# store each component as a variable
# ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
# ‘P’ is the amount that the user deposits.
# ‘t’ is the number of years that the money is being invested for. 
# ‘A’ is the total amount once the interest has been applied.
# Print out the answer 
    if interest == "simple":
        r= interest_rate / 100
        P= deposit_amount
        t= float(investment_years)               
        simple_interest= round(P * (1 + r * t) , 2)               
        print(f"The total amount on investment once the interest has been applied: R{simple_interest} \t")

    elif interest == "compound":
        r= interest_rate / 100
        P= deposit_amount
        t= float(investment_years)               
        compound_interest= round(P * (1 + r)**t , 2) 
        print(f"The total amount on investment once the interest has been applied: R{compound_interest} \t")
        print(" ")
        
else:
    print("There is no valid input. Please try again.")                          
    print(" ")


               



