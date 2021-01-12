'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# get a string of words from user
# get a letter from user
# find the first index of that letter

user_input = input("Type a sentence or phrase: ")
letter_input = input("Pick a letter: ")

result = user_input.find(letter_input)
print(f"Result : {result}")


