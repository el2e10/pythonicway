s = "Python"

reversed_s = ""
index = len(s) - 1

# start from last index and append each character to reversed string
while index >= 0:
    reversed_s += s[index]
    index -= 1

print(f"s is '{s}'")
print(f"reverse of s is '{reversed_s}'")

# Result
# s is 'Python'
# reverse of s is 'nohtyP'