# 📝 Day 13: Lambda, Map, Filter, and Reduce

#================================================================

# 🎯 Task:
# 1. Use `map()` to double each element of a list.
# 2. Use `filter()` to get only even numbers from the list.
# 3. Use `reduce()` to find the sum of the list.

# 🔥 Input/Output:
# Input:
# List: [1, 2, 3, 4, 5]
# Output:
# Doubled: [2, 4, 6, 8, 10]
# Even Numbers: [2, 4]
# Sum of List: 15

#================================================================
from functools import reduce

input_list = [1, 2, 3, 4, 5]

#Doubled List:
doubled_list = list(map(lambda x : x*2, input_list))
print("Doubled List is: ", doubled_list)

#Even numbers list:
even_numbered_list = list(filter(lambda x : x % 2 == 0, input_list))
print("Even Numbers is: ", even_numbered_list)

#Sum of list:
sum_of_list = reduce(lambda x, y: x+y, input_list)
print("Sum of List is: ", sum_of_list)