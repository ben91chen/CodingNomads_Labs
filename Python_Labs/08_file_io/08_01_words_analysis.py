'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
path = os.getcwd()
print(path)

with open('words.txt', 'r') as f:
    read_data = f.read()
    x = read_data.split()
    print(len(x))
    max_ = max(x, key=len)
    min_ = min(x, key=len)
    for i in x:
        if len(i) == len(max_):
            print(i)
    for i in x:
        if len(i) == len(min_):
            print(i)




