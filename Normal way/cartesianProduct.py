# Cartesian product
A = [1, 2, 3]
B = [5, 7, 2]

cartesian_product = []

for x in A:
	for y in B:
		pair = (x, y)
		cartesian_product.append(pair)

print(cartesian_product)

# Result
# [(1, 5), (1, 7), (1, 2), (2, 5), (2, 7), (2, 2), (3, 5), (3, 7), (3, 2)]