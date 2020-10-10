key = 2
arr = [1, 2, 3, 4, 5, 2]

new_arr = [element for element in arr if element != key]
print(new_arr)

# Result
# [1, 3, 4, 5]
