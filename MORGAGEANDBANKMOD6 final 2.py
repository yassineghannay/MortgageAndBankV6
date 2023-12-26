''''
Mortgage and Bank
Ye Phone, Malek, Yassine 
'''

from typing import Final

#Constants

# Purchase Prices final
FIRST_PURCHASE_PRICE:Final = 500000
SECOND_PURCHASE_PRICE:Final = 1000000

# Down Payment Percentages final
MINIMUM_DOWN_PAYMENT_PERCENTAGE:Final = 0.05
LESS_THAN_ONE_MILLION_PERCENTAGE:Final = 0.1
MORE_THAN_ONE_MILLION_PERCENTAGE:Final = 0.2

# Mortgage insurance percentages final
FIRST_MORTGAGE_INSURANCE:Final = 0.04
SECOND_MORTGAGE_INSURANCE:Final = 0.031
THIRD_MORTGAGE_INSURANCE:Final = 0.028


# Mortgage interest rates final
ONE_YEAR_MORTGAGE_INTEREST_RATE:Final = 0.0595
TWO_YEARS_MORTGAGE_INTEREST_RATE:Final = 0.059
THREE_YEARS_MORTGAGE_INTEREST_RATE:Final = 0.056
FIVE_YEARS_MORTGAGE_INTEREST_RATE:Final = 0.0529
TEN_YEARS_MORTGAGE_INTEREST_RATE:Final = 0.06


MAXIMUM100_DOWN_PAYMENT_PERCENTAGE:Final = 100
FIVE_PERCENT_VALUE:Final = 5
TEN_PERCENT_VALUE:Final = 10
FIFTHEEN_PERCENT_VALUE:Final = 15
TWENTY_PERCENT_VALUE:Final = 20




#Initial User input
name = input('Please enter your name: ')
address = input('Please enter your address: ')
purchase_price = float(input('Please enter the purchase price: '))

#Checking purchase price value from table 1 
if purchase_price <= FIRST_PURCHASE_PRICE:
    minimum_down_payment = purchase_price * MINIMUM_DOWN_PAYMENT_PERCENTAGE
elif FIRST_PURCHASE_PRICE < purchase_price <= SECOND_PURCHASE_PRICE:
    minimum_down_payment = (FIRST_PURCHASE_PRICE * MINIMUM_DOWN_PAYMENT_PERCENTAGE) + ((purchase_price-FIRST_PURCHASE_PRICE)*LESS_THAN_ONE_MILLION_PERCENTAGE)
else:
    minimum_down_payment = purchase_price * MORE_THAN_ONE_MILLION_PERCENTAGE

#Computes minimum down payment percentage show it to the user in the next input
minimum_down_payment_percentage = minimum_down_payment / purchase_price * 100

down_payment_percentage = float(input(f'Enter down payment percentage (minimum {minimum_down_payment_percentage:.3f}%): '))


# Checks if the user input satisfies the down payement percentage minimum
while MAXIMUM100_DOWN_PAYMENT_PERCENTAGE <= down_payment_percentage or down_payment_percentage < minimum_down_payment_percentage:
    print('Please enter a value between the minimum and 100')
    down_payment_percentage = float(input(f'Enter down payment percentage (minimum {minimum_down_payment_percentage:.3f}%): '))
    
else:         
    down_payment_amount = (down_payment_percentage * purchase_price) / 100
    print(f'Down payment amount is ${down_payment_amount:.0f}')

# Checking the down payment percentage and calculation for total mortgage amount
if FIVE_PERCENT_VALUE <= down_payment_percentage < TEN_PERCENT_VALUE:
    insurance_cost = (purchase_price - down_payment_amount) * FIRST_MORTGAGE_INSURANCE
elif TEN_PERCENT_VALUE <= down_payment_percentage < FIFTHEEN_PERCENT_VALUE:
    insurance_cost = (purchase_price - down_payment_amount) * SECOND_MORTGAGE_INSURANCE
elif FIFTHEEN_PERCENT_VALUE <= down_payment_percentage < TWENTY_PERCENT_VALUE:
    insurance_cost = (purchase_price - down_payment_amount) * THIRD_MORTGAGE_INSURANCE
else:
    insurance_cost = 0

principal_amount = (purchase_price - down_payment_amount) + insurance_cost

print(f'Mortgage insurance price is ${insurance_cost:.0f}')
print(f'Total mortgage amount is ${principal_amount:.0f}')

# Checking the mortgage term input is valid or not. 
mortgage_term = 0
mortgage_term_list = [1, 2, 3, 5, 10]
mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

while not mortgage_term in mortgage_term_list:
    print('Please enter a valid choice')
    mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

else:
    if mortgage_term == 1:
        mortgage_interest_rate = ONE_YEAR_MORTGAGE_INTEREST_RATE
    
    elif mortgage_term == 2:
        mortgage_interest_rate = TWO_YEARS_MORTGAGE_INTEREST_RATE
        
    elif mortgage_term == 3:
        mortgage_interest_rate = THREE_YEARS_MORTGAGE_INTEREST_RATE
        
    elif mortgage_term == 5:
        mortgage_interest_rate = FIVE_YEARS_MORTGAGE_INTEREST_RATE
        
    
    else:
        mortgage_interest_rate = TEN_YEARS_MORTGAGE_INTEREST_RATE
        
# if the user input is valid, the program will request for mortage amortization peroid
   
amortization_period = 0
amortization_period_list = [5, 10, 15, 20, 25]
amortization_period = int(input('Enter mortgage amortization period (5, 10, 15, 20, 25): '))

# Checking amortization peroid includes in the amortization period list   
while not amortization_period in amortization_period_list:
    print('Please enter a valid choice')
      
    amortization_period = int(input('Enter mortgage amortization period (5, 10, 15, 20, 25): '))
else:

# Calculation for monthly payment amount
    if amortization_period in amortization_period_list:
        print(f'Interest rate for the term will be {100 * mortgage_interest_rate:.2f}%')
    emr = (((1 + mortgage_interest_rate/2) ** 2) ** (1/12)) - 1 

    n = amortization_period * 12
    monthly_payment = principal_amount * (emr * (1 + emr)**n) / ((1 + emr)**(n) - 1) 

    print(f'Monthly payment amount is: ${monthly_payment:.0f}')

# Calculate monthly payment and initialize balances

opening_balance = 0
n = amortization_period * 12
monthly_payment = principal_amount * (emr * (1 + emr)**n) / ((1 + emr)**(n) - 1)
opening_balance = principal_amount
new_monthly_term = mortgage_term * 12

# Get user input for displaying amortization schedule

user_input = input('Would you like to see the amortization schedule? (Y/N): ').upper()
#Getting user input for amortization schedule (Y or N) and constructing the table using formatted string
if user_input == 'Y':
    print(f'{"Monthly Amortization Schedule":^120}')
    print()
    print(f'{"Month":^10} {"Opening Bal":^20} {"Payment":^20} {"Principal":^20} {"Interest":^20} {"Closing Bal":^20}')

    total_interest_paid = 0
    total_principal_paid = 0
    
  # Using for loop to make necessary calculatios.
    for x in range(1, new_monthly_term + 1):
        monthly_interest_amount = opening_balance * emr
        monthly_principle_amount = monthly_payment - monthly_interest_amount
        closing_balance = opening_balance - monthly_principle_amount

        print(f'{x:^10} {opening_balance:^20.2f} {monthly_payment:^20.2f} {monthly_principle_amount:^20.2f} {monthly_interest_amount:^20.2f} {closing_balance:^20.2f}')
        opening_balance = closing_balance
        total_interest_paid += monthly_interest_amount
        total_principal_paid += monthly_principle_amount


    print('=' * 120)
    print(f'Total {total_principal_paid:>60.2f}  {total_interest_paid:^30.2f}')
