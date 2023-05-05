# resturant.py
# David Chong
# Aug. 31,2021
# This program prompts the user for the cost of food drinks, then calucualtes the cost of the meal.
# The total bill is calculated detailing the tax and tip amount including cost of the meal.

# Algorithm:
# Declare and initialize variable constants
# float cost of meal, tax amount, tip amount
# constant float TAX_PERCENT = 0.075
# constant float TIP_AMOUNT = 0.18
# Display Intro
# Prompt user for cost of food
# Prompt user for cost of drinks
# Calculate cost of meal
# cost of meal = cost of food + cost of drinks
# Calculate tax amount
# tax amount = TAX_PERCENT * cost of meal
# Calculate tip amount
# tip amount = TIP_PERCENT * costofmeal
# Display results (cost of meal + tax + tip)



def main():
    #Declare and initialize variables and constants
    #Float cost of meal, tax amount, tip amount = 0
    #constant float TAX_PERCENT = 0.075
    TAX_PERCENT = 0.075
    #constant float TIP_PERCENT = 0.18
    TIP_PERCENT = 0.18
    #Display intro    
    print(' ')
    print('Resturant Bill Generator...\n')
    #Prompts the user for the cost of food
    costoffood = float(input('Please enter cost of food: '))
    #Prompts the user for cost of drinks
    costofdrinks = float(input('Please enter cost of drinks: '))
    #Calculate cost of meal
    costofmeal = costoffood + costofdrinks
    #Calculate tax amount
    taxamount = TAX_PERCENT * costofmeal
    #Calculate tip amount
    tipamount = TIP_PERCENT * (costofmeal)
    #Calculate total cost of meal
    total = costofmeal + taxamount + tipamount
    #Display results
    print(' ')
    print('Resturant Bill')
    print('-----------------------')

    print('Cost of Meal: $' + format(costofmeal, ',.2f'), 'Tax Amount:   $' + \
       format(taxamount, ',.2f' ), 'Tip Amount:   $' + format(tipamount, ',.2f'), \
       ('              ---------'), 'Total:        $' + format(total, ',.2f'), sep = '\n' )


