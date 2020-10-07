f = open('arrayIteration.py', 'rb') # Open file for example "arrayIteration.py"
python_file = f.read() # Read content from file
print(python_file)  
# Do other stuff with the file.
f.close() # Close the file

# Result 
# arr = [5, 2, 9, 5, 6]

# for i in range(len(arr)):
#     print(f'{i} : {arr[i]}')


# Result
# 0 : 1
# 1 : 2
# 2 : 4
# 3 : 5
# 4 : 6