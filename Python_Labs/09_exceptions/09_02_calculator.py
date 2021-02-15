'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the division: "))
    result = dividend / divisor
    print(f"The result of {dividend} divided by {divisor} is {result}")
except ZeroDivisionError:
    print("Number can't be divided by 0.")
except ValueError:
    print("That's not a number.")

