'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

try:
    with open('integers.txt') as f:
        num = int(f.read(1))
        calculation = num + 1
except FileNotFoundError:
    print("File doesn't exist")
except ValueError:
    print("Can only read in the 1st character")
else:
    print(calculation)





