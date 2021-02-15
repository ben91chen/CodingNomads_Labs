'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
import os
# Open war_and_peace.txt, read the whole file content and store it in a variable
with open('books/war_and_peace.txt', 'r') as f:
    book_1 = f.read()
# Open crime_and_punishment.txt and overwrite the whole content with an empty string
try:
    with open('books/crime_and_punishment.txt', 'w') as writer:
        writer.write("")
except TypeError:
    print("One of your files does not have any characters.")

path = "/Users/benchen/Documents/CodingNomads/labs/Python_Labs/09_exceptions/books"
os.chdir(path)
files = os.listdir(path)
print(files)

for file in files:
    with open(file, 'r') as reader:
        if "copy" in file:
            break
        else:
            print(reader.read(1))


