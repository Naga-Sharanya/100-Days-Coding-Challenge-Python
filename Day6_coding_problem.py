#📝 Day 6: Remove Duplicates and Sort List

#=============================================================

# 🎯 Task:
# 1. Take a list of integers as input.
# 2. Remove duplicates and sort the list in ascending order.

# 🔥 Input/Output:
# Input:
# Enter list of numbers: 4, 2, 7, 4, 9, 2, 5
# Output:
# Sorted list without duplicates: [2, 4, 5, 7, 9]

#=============================================================


#Method 1:
#Using built-in functions -- set and sorted.
# numbers = list(map(int, input("Enter the list of numbers: ").split()))
# print(numbers)
# unique_numbers = set(numbers)
# print("unique numbers: ", unique_numbers)
# sorted_numbers = sorted(unique_numbers)
# print('Sorted list without duplicates: ', sorted_numbers)


#Method 2:
#Without Using built-in functions
"""
Sort the List Manually
Use Bubble Sort (or any other sorting algorithm) to sort the list.
Bubble Sort compares adjacent elements and swaps them if they are out of order.
"""

numbers = list(map(int, input("Enter the list of numbers: ").split()))
# Step 1: Remove duplicates
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        print("unique number added: ", num)
print("unique numbers printing: ", unique_numbers)

# Step 2: Sort the List Manually (Bubble Sort)
n = len(unique_numbers)
for i in range(0, n):
    for j in range(0, n-i-1):
        if unique_numbers[j] > unique_numbers[j+1]:
            unique_numbers[j], unique_numbers[j+1] = unique_numbers[j+1], unique_numbers[j]
            print("unique number swapped! for j ", unique_numbers[j], "and j+1 ", unique_numbers[j+1])
            print("unique number list after swapping is: ", unique_numbers)
            
print("Sorted List without duplicates is: ", unique_numbers)

# Step 2: Sort the List Manually (Selection Sort)
n = len(unique_numbers)
for i in range(0,n):
    min_index = i
    for j in range(i+1, n):
        if unique_numbers[j] < unique_numbers[min_index]:
            min_index = j
        unique_numbers[i], unique_numbers[min_index] = unique_numbers[min_index], unique_numbers[i]
        print("unique numbers swapped j is: ", unique_numbers[j], "min index is: ", unique_numbers[min_index])
        print("swapped list is: ", unique_numbers)
        
print("Sorted list without duplicates is: ", unique_numbers)
#Steps for converting the string input from user to the list:
# numbers = input("Enter the list of numbers: ") #taking input numbers as string
# numbers_new = numbers.split() #splitting numbers 
# numbers_list = map(int, numbers_new)
# numbers_list_new = list(numbers_list)
# for num in numbers_list_new:
#     print(num)