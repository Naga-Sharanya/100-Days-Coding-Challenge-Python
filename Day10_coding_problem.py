#📝 Day 10: Check Palindrome String

#================================================================

# 🎯 Task:
# 1. Input a string.
# 2. Check if it’s a palindrome or not (ignoring case and spaces).

# 🔥 Input/Output:
# Input:
# Enter a string: madam
# Output:
# Yes, it is a palindrome.

#================================================================

# Method 1:
input_string = input("Enter a string: ")
cleaned_string = input_string.replace(" ", "").lower()
reversed_string = cleaned_string[::-1]
if reversed_string == cleaned_string:
    print("Yes, it is a Palindrome.")
else:
    print("No, it's not a Palindrome.")
    
    
#Method 2: In one Line...
print("Yes it is a Palindrome." if (input_string:= input("Enter a string: ").replace(" ", "").lower()) == input_string[::-1] else "No, its not a Palindrome.")