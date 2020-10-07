
lst = [1,2,2,3,4,5,2,5,6,6,7,8,2,9]
arr = []

for i in lst:
    if i in arr:
        continue
    else:
        arr.append(i)

print(arr)