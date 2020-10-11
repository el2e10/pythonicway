from functools import reduce
nestedList = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

target_list = []
for oneNestedList in nestedList:
    target_list += oneNestedList
print(f"First pythonic way {target_list}")

# OR

target_list_v2 = reduce(lambda x,y: x+oneNestedList,nestedList)
print(f"Second pythonic way {target_list}")

# OR

target_list_v3 = sum(nestedList, [])
print(f"Third pythonic way {target_list}")

# Result
# First pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# Second pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# Third pythonic way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']