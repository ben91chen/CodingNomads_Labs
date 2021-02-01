'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

# fun1() converts days into hours
def fun1(days):
    hours = days * 24
    return hours

#fun2() conversts hours into minutes
def fun2(days):
    minutes = fun1(days) * 60
    return minutes

#fun3() converts minutes into seconds
def fun3(days):
    seconds = fun2(days) * 60
    return seconds

print(f"There are {fun3(7)} seconds in the number of days you inputted.")