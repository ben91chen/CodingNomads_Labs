'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
gen = (num for num in range(100000) if num % 1111 == 0)


for number in gen:
    print(number // 1111)