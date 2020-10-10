from collections import Counter
# Count of every elements in an array

arr = [4, 5, 2, 1, 2, 5, 1]
count_of_elements = Counter(arr)
print(dict(count_of_elements))

# Result
# {5: 2, 4: 1, 2: 1, 1: 1}
