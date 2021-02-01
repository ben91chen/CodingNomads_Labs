'''

Write a script that completes the following tasks.

'''


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results




# This function returns a boolean based on if the arguement/parameter is divisible by 4 or 7.
def fun1(num):
    if num % 4 == 0 or num % 7 == 0:
        return True
    else:
        return False

# This function returns a boolean based on if the arguement/parameter is divisible by 4 and 7.
def fun2(num):
    if num % 4 == 0 and num % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000
def fun3():
    number = input("Pick a number between 1 and 1,000,000,000: ")
    return number

print(fun1(10))
print(fun2(28))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables
# print your new variables to display the results
print(fun3())
