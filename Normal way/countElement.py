# Get the count of an element in an array
arr = [5, 2, 9, 5, 6]
element = 5
count = 0

for value in arr:
    if value == element:
        count += 1

print(f'The count of {element} is {count}')

# Result
# The count of 5 is 2
