'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen = (x for x in range(5))
print(gen)

for num in gen:
    print(num)

gen_list = [number for number in gen]
print(gen_list)
print(gen)
