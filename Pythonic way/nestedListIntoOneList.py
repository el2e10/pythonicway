from functools import reduce
nested_list = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

target_list = []
for one_nested_list in nested_list:
    target_list += one_nested_list
print(f"First pythonic way {target_list}")

# OR

target_list_v2 = reduce(lambda x,y: x+one_nested_list, nested_list)
print(f"Second pythonic way {target_list}")

# OR

target_list_v3 = sum(nested_list, [])
print(f"Third pythonic way {target_list}")

# Result
# First pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# Second pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# Third pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']