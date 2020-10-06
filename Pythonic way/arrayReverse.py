arr = [5, 2, 9, 5, 6]

for value in reversed(arr):
    print(f'{value}', end=' ')

# OR

print(*(reversed(arr)))  # Unpack with *

# Result
# 6 5 9 2 5
