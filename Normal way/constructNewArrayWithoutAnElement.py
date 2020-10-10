key = 2
arr = [1, 2, 3, 4, 5, 2]

# construct new arr without key
new_arr = []

for element in arr:
    if element != key:
        new_arr.append(element)

print(new_arr)

# Result
# [1, 3, 4, 5]
