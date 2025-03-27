#📝 Day 5: Print Prime Numbers in a Range

#================================================================

# 🎯 Task:
# 1. Input two numbers 'start' and 'end'.
# 2. Print all prime numbers in the range [start, end].

# 🔥 Input/Output:
# Input:
# Enter start: 10
# Enter end: 20
# Output:
# Prime numbers: 11, 13, 17, 19

#================================================================

starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))

print("Prime Numbers: ", end = "")
for num in range(starting_number, ending_number + 1):
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end = ",")