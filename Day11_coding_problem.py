#📝 Day 11: Basic Functions and Return Values

#================================================================

# 🎯 Task:
# 1. Write a function `is_prime(n)` to check if a number is prime.
# 2. Return True if prime, otherwise False.

# 🔥 Input/Output:
# Input:
# Enter a number: 17
# Output:
# True

#================================================================

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True
    

num = int(input("Enter any number: "))
print(is_prime(num))