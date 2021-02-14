'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
path = os.getcwd()
print(path)

with open('words.txt', 'r') as f:
    read_data = f.read()
    x = read_data.split()
    for word in x:
        if len(word) > 19:
            print(word)

