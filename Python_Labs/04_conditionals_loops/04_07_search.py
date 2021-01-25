'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
counter = 0
user_input = int(input("Type a number from 0 to 1,000,000,000: "))

while counter != user_input:
    counter += 1
print(counter)
