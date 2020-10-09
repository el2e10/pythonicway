words = ["one", "two", "three", "four", "five"]
nums = [1, 2, 3, 4, 5]
table = {}

for i in range(len(words)):
    table[words[i]] = nums[i]

print("List 1: " + str(words))
print("List 2: " + str(nums))
print("Map: " + str(table))

# Result
# List 1: ['one', 'two', 'three', 'four', 'five']
# List 2: [1, 2, 3, 4, 5]
# Table: {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
