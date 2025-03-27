#📝 Day 3: Basic Arithmetic Operations
#================================================================

# 🎯 Task:
# 1. Create a basic calculator that takes two numbers and an operator (+, -, *, /) as input.
# 2. Return the result based on the operator.

# 🔥 Input/Output:
# Input:
# Enter first number: 8
# Enter second number: 4
# Enter operator (+, -, *, /): *
# Output:
# Result: 32

#================================================================

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
    print("Result: ", result)
elif operator == "_":
    result = first_number - second_number
    print("Result: ", result)
elif operator == "*":
    result = first_number * second_number
    print("Result: ", result)
elif operator == "/":
    result = first_number / second_number
    print("Result: ", result)