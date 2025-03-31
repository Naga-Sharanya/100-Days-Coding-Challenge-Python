#📝 Day 15: Error Handling with try-except

#===============================================================

# 🎯 Task:
# 1. Write a function `divide(a, b)` to divide two numbers.
# 2. Handle ZeroDivisionError with try-except.

# 🔥 Input/Output:
# Input:
# Enter two numbers: 8, 0
# Output:
# Error: Division by zero is not allowed.

#===============================================================

def divide(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
result = divide(a, b)
print(result)