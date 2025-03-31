#📝 Day 17: Args, Kwargs, and Unpacking

#===============================================================

# 🎯 Task:
# 1. Write a function `sum_numbers(*args)` that accepts any number of arguments.
# 2. Return the sum of all numbers passed.

# 🔥 Input/Output:
# Input:
# sum_numbers(1, 2, 3, 4)
# Output:
# Sum: 10

#===============================================================


def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 7, 3, 4)
print("Sum: ", result)