#📝 Day 16: Nested Functions and Closures

#================================================================

# 🎯 Task:
# 1. Write a function `power(n)` that returns another function to calculate the nth power of a number.

# 🔥 Input/Output:
# Input:
# Square of 4: 16
# Cube of 3: 27

#================================================================

def power(n):
    def nth_power(x):
        return x ** n
    return nth_power

square = power(2)
cube = power(3)

print("Square of 4 is: ", square(4))
print("Cube of 3 is: ", cube(3))