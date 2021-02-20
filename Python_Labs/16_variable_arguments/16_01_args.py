'''
Write a script with a function that demonstrates the use of *args.

'''

def to_do_list(*args):
    for a in args:
        print(a)

to_do_list("clean house", "feed dog", "make dinner", "go for run")