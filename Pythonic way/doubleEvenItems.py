arr = [1, 2, 3, 4, 5, 6]

print("Old Values:", arr)
# Old Values: [1, 2, 3, 4, 5, 6]

new_arr = [x * 2 if x % 2 == 0 else x for x in arr]

print("New Values:", new_arr)
# New Values: [1, 4, 3, 8, 5, 12]

# here we use list comprehension to embed a loop, inside a list,
# this then outputs a list which we assign back
