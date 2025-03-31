#📝 Day 12: Recursive Functions

#================================================================

# 🎯 Task:
# 1. Implement a recursive function `factorial(n)` to calculate the factorial of a number.
# 2. Return the factorial value.

# 🔥 Input/Output:
# Input:
# Enter a number: 5
# Output:
# Factorial of 5 is 120

#================================================================


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a number: "))
print(F" Factorial of {num} is: {factorial(num)}")