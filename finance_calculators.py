# Finance Calculator

# This is an example of Python finance calculator using while loop with if statent and try statement.
# The user inputs 'investment' or 'bond'.
# The program outputs calculations of the 'investment' and 'bonds' based on user inputs.
# Program using clear console function from (https://stackoverflow.com/questions/2084508/clear-terminal-in-python).

   
import os

def clr():
    os.system("cls" if os.name == "nt" else "clear")

import math

# User input for quit function.
user_input = ""
clr()

# While loop asking user to input type of calculation. 
while True:
    
    print("Investment - To calculate the amount of interest you'll earn on your investment. " + "\nBond - To calculate the amount you'll have to pay on a home loan. ")

    calculator = input("\nEnter either 'Investment' or 'Bond' from the menu above to proceed: ")

# While loop for investment calculator with if statement asking user to choose calculator and input investment/bond.
# Try statements to check if users input is correct.
    while True:
        if calculator.lower() == "investment":

            while True:
                try:
                    money_deposit = float(input("\nHow much money do you want to deposit? : "))  
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers. ")
                    continue
                break
            
            while True:
                try:
                    interest_rate = float(input("\nWhat interest rate of deposit? : "))   
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers. ")
                    continue
                break
            
            while True:
                try:
                    number_years = float(input("\nHow many years of deposit? : "))    
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers. ")
                    continue
                break

# While loop with if statent to check if users input is correct and to calculate simple/compound intrest.
            while True:
                interest = input("\nPlease enter 'simple' or 'compund' interest rate? : ")
                if interest.lower() == "simple":
                    simple_interest = money_deposit * (1 + (interest_rate / 100) * number_years) 
                    clr()
                    print(f"Your total amount after {number_years} years at simple interest rate of {interest_rate} % per year will be: {simple_interest}\n")
                elif interest.lower() == "compound":
                    compound_interest = money_deposit * math.pow((1 + (interest_rate / 100)), number_years)
                    clr()
                    print(f"Your total amount after {number_years} years at compund interest rate of {interest_rate} % per year will be: {compound_interest}\n")
                else:
                    print("\nInvalid input. Please enter only 'Simple' or 'compound'. ")
                    continue
                user_input = input("Press any key to continue or 'Quit' to quit program: ")
                clr()
                break
            break
        
# While loops to check for correct user input.        
        elif calculator.lower() == "bond":
            while True:
                try:
                    house_value = float(input("\nWhat is present value of the house?: "))
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers")
                    continue
                break
            while True:
                try:
                    monthly_interest = float(input("\nWhat interest rate of the bond?: "))
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers")
                    continue
                break
            while True:
                try:
                    number_months = float(input("\nHow many months of the bond?: "))
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers")
                    continue
                break

# Bond calculation and program loop/quit function.
            calculation = ((monthly_interest / 100) * house_value) / (1 - (1 + (monthly_interest / 100)) ** (-number_months)) / 12
            monthly_repayment = round(calculation, 2)
            clr()
            print(f"\nYour monthly repayment for a house valued at {house_value} with an interest rate of {monthly_interest}% will be {monthly_repayment} per month for {number_months} months.\n")
            
            user_input = input("\nPress any key to continue or 'Quit' to quit program: ")
            clr()
            break
    
        else:
            clr()
            print("\nInvalid input. Please enter either 'Investment' or 'Bond'. \n")
            break
    if user_input.lower() == "quit":
        break



