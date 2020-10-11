nestedList = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

target_list = []
for oneNestedList in nestedList:
    for nestedListElement in oneNestedList:
        target_list.append(nestedListElement)

print(f"Normal way {target_list}")

# Result 
# Normal way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']