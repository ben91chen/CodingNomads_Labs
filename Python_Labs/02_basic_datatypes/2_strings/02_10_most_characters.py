'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

user_input1 = input("Type your 1st string: ")
user_input2 = input("Type your 2nd string:  ")
user_input3 = input("Type your 3rd string: ")

print(len(user_input1), ",", user_input1)
print(len(user_input2), ",", user_input2)
print(len(user_input3), ",", user_input3)

print("----------------------------------")
print("The string with the most characters is: ")

string_list = [user_input1, user_input2, user_input3]
longest_string = max(string_list, key=len)


print(len(longest_string), ",", longest_string)