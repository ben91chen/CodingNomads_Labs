'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
sum = 0
user_input1 = int(input("Type a number: "))
user_input2 = int(input("Type another number: "))

for num in range(user_input1, user_input2 + 1):
    sum += num

print(sum)