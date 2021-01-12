'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount = int(input("How many dollars do you want to invest? "))
interest_rate_percentage = float(input("What is the interest rate in percentage? "))
interest_rate_conversion = interest_rate_percentage / 100
years_to_invest = float(input("How many years will you invest? "))

# FV = PV(1+4)**n
future_value = investment_amount * ((1 + interest_rate_conversion) ** years_to_invest)
print(f"Your future value of this investment is {future_value} dollars.")
