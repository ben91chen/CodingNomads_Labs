'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

# remove duplicates
set_ = set(list_)

# convert back to list
list_2 = list(set_)
print(list_2)
