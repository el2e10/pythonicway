
arr = [1, 2, 2, 3, 4, 5, 2, 5, 6, 6, 7, 8, 2, 9]
no_duplicates_list = []

for i in arr:
    if i in no_duplicates_list:
        continue
    else:
        no_duplicates_list.append(i)

print(no_duplicates_list)

# Result
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
