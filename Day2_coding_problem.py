
#📝 Day 2: Swap Two Variables Without Using Third Variable
#================================================================
# 🎯 Task:
# 1. Swap two variables a and b without using a third variable.

# 🔥 Input/Output:
# Input:
# Enter value of a: 5
# Enter value of b: 10
# Output:
# After swapping: a = 10, b = 5

#================================================================


#Method 1: 
a_value = int(input("Enter the value of a: "))
b_value = int(input("Enter the value of b: "))
c_value = a_value
a_value = b_value
b_value = c_value
print(" After Swapping : a = ", a_value, "b = ", b_value)

#Method 2:
a_value = int(input("Enter the value of a: "))
b_value = int(input("Enter the value of b: "))
a_value, b_value = b_value, a_value
print("After Swapping : a = ", a_value, "b = ", b_value)