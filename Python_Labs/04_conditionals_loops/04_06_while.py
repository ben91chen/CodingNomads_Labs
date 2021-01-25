'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

counter = 1

while counter < 101:
    if counter % 5 == 0:
        print(counter)
    counter += 1