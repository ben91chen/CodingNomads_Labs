'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def age(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is {v} years old.")

age(Ben = 30, Bob = 35, John = 28)

