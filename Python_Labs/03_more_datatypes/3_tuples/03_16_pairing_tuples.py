'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
# get a list and sort
list_of_numbers = [5, 89, 3, 25, 100, 56, 5]
list_of_numbers.sort()

# if list is odd, add a 0 to the end of it.
if len(list_of_numbers) % 2 == 1:
    list_of_numbers.append(0)

# store pairs of tuples into list
pairs = [(list_of_numbers[i], list_of_numbers[i + 1]) for i in range(0, len(list_of_numbers), 2)]
print(pairs)

