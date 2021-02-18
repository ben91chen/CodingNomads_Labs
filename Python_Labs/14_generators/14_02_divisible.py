'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

gen = (num for num in range(100000) if num % 1111 == 0)
print(gen)

for number in gen:
    print(number)