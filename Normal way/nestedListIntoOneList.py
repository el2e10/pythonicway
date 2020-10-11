nested_list = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

target_list = []
for one_nested_list in nested_list:
    for nested_list_element in one_nested_list:
        target_list.append(nested_list_element)

print(f"Normal way {target_list}")

# Result 
# Normal way ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']