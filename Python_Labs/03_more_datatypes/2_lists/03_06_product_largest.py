'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
print("-------------------------------")
print("Product Largest python exercise")
print("-------------------------------")

# get 10 numbers from user and append to a list
# convert the inputs from string to integer
# find the largest number and print

print("Please input 10 numbers:")
list = []
int_list = []
counter = 1

# get 10 numbers from user and append to list
while counter < 11:
    user_input = input(f"Number {counter}: ")
    list.append(user_input)
    counter += 1

# convert user input from string to integer
for str in list:
    int_list.append(int(str))

# print largest number in list
print(max(int_list))

# iterate over int_list and multiple all the numbers
result = 1
for i in int_list:
    result = result * i
print(result)





