#📝 Day 9: List and Dictionary Comprehensions

#================================================================

# 🎯 Task:
# 1. Create a list of squares of numbers from 1 to 10 using list comprehension.
# 2. Create a dictionary where the keys are numbers from 1 to 5 and values are their cubes.

# 🔥 Input/Output:
# Output:
# List of squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Dict of cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

#================================================================

#List of Squares:
square_list = []
for i in range(1, 11):
    square_list.append(i**2)
print("List of squares: ", square_list)

#Dict of cubes:
cubes_dict = {}
for i in range(1,6):
    cubes_dict[i] = i**3
print("Dict of cubes: ", cubes_dict)