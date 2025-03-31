#📝 Day 8: Merge Two Dictionaries and Sort by Key

#================================================================

# 🎯 Task:
# 1. Input two dictionaries and merge them.
# 2. Sort the merged dictionary by keys.

# 🔥 Input/Output:
# Input:
# Dict A: {'a': 1, 'c': 3}
# Dict B: {'b': 2, 'd': 4}
# Output:
# Merged and sorted dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#================================================================


#dict_A and dict_B are merged using {**dict_A, **dict_B}, which combines both dictionaries.
# merged_dict.items() converts the dictionary into a list of tuples.
# sorted() sorts these tuples by the dictionary keys.
# dict(sorted(...)) converts the sorted tuples back into a dictionary.

#Method 1 using ** operators.
dict_A = {'a' : 1, 'c' : 3}
dict_B = {'b' : 2, 'd' : 4}

merged_dict = {**dict_A, **dict_B}
sorted_dict = dict(sorted(merged_dict.items()))
print("Merged and sorted dictionary: ", sorted_dict)


#-------------------------------------------------------------
#Method 2 with using update()
dict_A = {'a' : 1, 'c' : 3}
dict_B = {'b' : 2, 'd' : 4}

# merged_dict = {**dict_A, **dict_B}
dict_A.update(dict_B)
merged_dict = dict_A
sorted_dict = dict(sorted(merged_dict.items()))
print("Merged and sorted dictionary: ", sorted_dict)