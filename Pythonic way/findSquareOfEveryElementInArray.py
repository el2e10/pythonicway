arr = [1, 2, 3, 4]
# map is a function that takes every element in an iterable and applied the function
# given in parameter 1
square = list(map(lambda x: x * x, arr))
print(square)