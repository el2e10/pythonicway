list1 = [1, 2, 3, 4]
tuple1 = (5, 6, 7, 8)
set1 = {9, 10, 11, 12}

total_list = [*list1, *tuple1, *set1]

print(total_list)

# Result
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
