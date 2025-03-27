#📝 Day 4: Conditional Statements (if-elif-else)

#================================================================

# 🎯 Task:
# 1. Take input for age and classify as:
#    - Minor: age < 18
#    - Adult: 18 ≤ age < 60
#    - Senior Citizen: age ≥ 60

# 🔥 Input/Output:
# Input:
# Enter your age: 25
# Output:
# You are an Adult.

#================================================================

age = int(input("Enter your age: "))
if age < 18:
    print("Your are Minor!")
elif 18 <= age < 60:
    print("You are an Adult!")
else:
    print("You are a Senior Citizen!")