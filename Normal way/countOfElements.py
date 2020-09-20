# Count of every elements in an array

arr = [4, 5, 2, 5, 1]
count_dict = {}

for i in arr:
    if i not in count_dict:
        count_dict[i] = 1
    else:
        count_dict[i] += 1

print(count_dict)

# Result
# {4: 1, 5: 2, 2: 1, 1: 1}
