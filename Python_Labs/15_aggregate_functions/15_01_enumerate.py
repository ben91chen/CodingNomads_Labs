'''
Demonstrate the use of the .enumerate() function.
'''

my_list = ['a', 'b', 'c']
print(my_list)

for letter in my_list:
    print(letter)

for i, letter in enumerate(my_list, start=1):
    print(i, letter)