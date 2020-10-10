# Replace first iteration of an element from an array by another integer.
arr = [5, 10, 15, 20, 25, 50, 20]

index = 0
for element in arr:
    if(element == 20):
        break
    else:
        index += 1

arr[index] = 200
print(arr)

# Result
# [5, 10, 15, 200, 25, 50, 20]
