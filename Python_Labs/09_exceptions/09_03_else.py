'''
Write a script that demonstrates a try/except/else.

'''

try:
    f = open('integers.txt')
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
    f.close()
