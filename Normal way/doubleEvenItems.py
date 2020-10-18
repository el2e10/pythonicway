arr = [1, 2, 3, 4, 5, 6]
length = len(arr)

print("Old Values:", arr)
# Old Values: [1, 2, 3, 4, 5, 6]

for i in range(0, length):
    if arr[i] % 2 == 0:
        arr[i] *= 2

print("New Values:", arr)
# New Values: [1, 4, 3, 8, 5, 12]
