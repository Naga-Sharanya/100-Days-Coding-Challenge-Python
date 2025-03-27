#📝 Day 7: Union and Intersection of Sets

#================================================================

# 🎯 Task:
# 1. Input two sets.
# 2. Find and print the union and intersection.

# 🔥 Input/Output:
# Input:
# Set A: {1, 2, 3}
# Set B: {3, 4, 5}
# Output:
# Union: {1, 2, 3, 4, 5}
# Intersection: {3}

#================================================================

#Method 1 using built-in functions union and intersection:
set_A = input("Enter the values of set A: ")
split_A = set_A.split()
map_A = map(int, split_A)
set_A_set = set(map_A)
print("Set A is: ", set_A_set)

set_B = input("Enter the values of set B: ")
split_B = set_B.split()
map_B = map(int, split_B)
set_B_set = set(map_B)
print("Set B is: ", set_B_set)

#Union is:
union_set = set_A_set.union(set_B_set)
print("union of both sets is: ", union_set)

#Intersection is:
intersection_set = set_A_set.intersection(set_B_set)
print("Intersection of both sets is: ", intersection_set)


######################################################################

#Method 2: Without Using builtin functions : Union and intersection:
set_A = set(map(int, input("Enter the values of set A: ").split()))
set_B = set(map(int, input("Enter the values of set B: ").split()))

union_set = set_A.copy()
for num in set_B:
    if num not in union_set:
        union_set.add(num)    #Here, union_set is set_A which is set, so, for set append is not allowed, so, use add.
        print("number is: ", num)
        print("union set is: ", union_set)
print("Union of Set A and Set B is: ", union_set)

intersection_set = []
for num in set_A:
    if num in set_B and num not in intersection_set:
        intersection_set.append(num)      #Here, intersection_set is list, so, append is allowed, but at last need to convert to set.
        print("number for intersection: ", num)
        print("interseection: ", set(intersection_set))
    
print("Intersection of Set A and Set B is: ", intersection_set)