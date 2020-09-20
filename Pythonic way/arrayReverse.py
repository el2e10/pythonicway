arr = [5, 2, 9, 5, 6]

for value in reversed(arr):
    print(f'{value}', end=' ')

# OR

for value in arr[::-1]:
    print(f'{value}', end=' ')

# Result
# 5 6 5 9 2
