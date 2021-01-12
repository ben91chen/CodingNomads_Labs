'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# get a string input from user
# get a symbol from the user
# find first letter
# replace all letters with symbol

user_string = input("Type a sentence or phrase: ")
user_symbol = input("Pick a symbol: ")

first_letter = user_string[0]
print(user_string.replace(first_letter, user_symbol))
