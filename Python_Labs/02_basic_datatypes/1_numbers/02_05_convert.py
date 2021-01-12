'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

integer_number = 4
integer_to_float = float(integer_number)
print(integer_number)
print(integer_to_float)

float_number = 5.0
float_to_integer = int(float_number)
print(float_number)
print(float_to_integer)

float_division = float_number // integer_number
print(float_division)

user_integer = int(input("Type a number: "))
user_float = float(user_integer)
print(user_integer)
print(user_float)
