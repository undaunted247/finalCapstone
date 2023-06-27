import math #imports the math module for the calculations

#Dispalys a menu that shows the user the available investment calculation options 
select_calculation = input (f"investment-to calculate the amount of interest you'll earn on your investment.\nbond-to calculate the amount you'll have to pay on a home loan.\n""Please select either bond or investment calculation : ").lower()

#user inputs required variables if they input investment 
if select_calculation == "investment":
    principal = float(input("Please enter the amount you'd like to invest:£"))
    interest_rate = (float(input("Please enter the interest rate without the %:"))/100)
    number_of_years = float(input("Please enter the number of years you'd like to invest for:"))
    calculation_type = input("Please select simple or compound interest: ")  #allows user to select the type of interest calculation 
    
    #calculation for simple interest
    if calculation_type == "simple":
       simple_interest = float(principal*(1+interest_rate*number_of_years))
       print ("Your simple interest is : {}".format(simple_interest))
       
    #calculation for compound interest   
    elif calculation_type == "compound":
     compound_interest = float(principal * math.pow ((1+interest_rate), number_of_years))
     print ("Your compound interest is : {}".format(compound_interest))

#user inputs required variables if they input bond
elif select_calculation == "bond":
    present_value_house = float(input("Please enter the present value of the house you'd like to invest in:£"))
    bond_interest_rate = (float(input("Please enter the monthly interest rate without the %:"))/100/12)
    number_of_months = float(input("Please enter the number of months over which you'd like to repay the bond for:"))
   
    #calcualtion for bond repayment
    bond_repayment = (bond_interest_rate*present_value_house) / (1 - (1 + bond_interest_rate)**(- number_of_months))
    print ("You'll have to repay £{}  monthly".format(bond_repayment))
   
#output when the user enters an invalid input     
else:
    print ("You've entered an invalid input")