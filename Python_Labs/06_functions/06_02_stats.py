'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(nums):
  avg = sum(nums) / len(nums)
  max_ = max(nums)
  min_ = min(nums)
  sum_ = sum(nums)
  return avg, max_, min_, sum_

print(stats(example_list))