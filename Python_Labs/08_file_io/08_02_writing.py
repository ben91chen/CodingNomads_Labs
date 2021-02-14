'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
print(cwd)

# first attempt
"""reversed_list = []
with open('words.txt', 'r') as reader:
    read_data = reader.read()
    lines_split = read_data.split()
    lines_split.reverse()
    for word in lines_split:
        reversed_list.append(word)

with open('words_reverse.txt', "w") as writer:
    for word in reversed_list:
        writer.write(word)"""

with open('words.txt') as rf, open('words_reverse.txt', 'w') as wf:
    for line in reversed(rf.readlines()):
        wf.write(line)




