'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''


list = []
int_list = []
even_list = []
odd_list = []
sorted_list = []
counter = 1

while counter < 11:
    user_input = input(f"Number {counter}: ")
    list.append(user_input)
    counter += 1

for str in list:
    int_list.append(int(str))
print(int_list)

for num in int_list[1::2]:
    sorted_list.append(num)
for num in int_list[-2::-2]:
    sorted_list.append(num)

print(sorted_list)







