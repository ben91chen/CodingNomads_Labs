'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(list):
    enum_list = enumerate(list, start=1)
    [print(index, letter) for index, letter in enum_list]


my_list = ['a', 'b', 'c']
list2 = ['tennis', 'basketball']
my_enumerate(my_list)
my_enumerate(list2)
