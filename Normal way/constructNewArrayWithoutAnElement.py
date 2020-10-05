key = 2
arr = [1, 2, 3, 4, 5, 2]

#construct new arr without key
newarr = []

for element in arr:
    if element != key:
        newarr.append(element)

print(newarr)