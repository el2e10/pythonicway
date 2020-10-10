# Cartesian product

A = [1, 2, 3]
B = [5, 7, 2]

# using list comprehension
cartesian_product = [(x, y) for x in A for y in B]
print(cartesian_product)

# cartesian product using built-in function
def cartesianProduct(A, B):
	import itertools
	p = itertools.product(A, B) # p is a itertools.product object
	cartesian_product = list(p)
	return cartesian_product

print(cartesianProduct(A, B))

# Result
# [(1, 5), (1, 7), (1, 2), (2, 5), (2, 7), (2, 2), (3, 5), (3, 7), (3, 2)]