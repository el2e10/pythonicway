with open('arrayIteration.py', 'rb') as f: # Open file with contentmanager
    python_file = f.read() # Read content from file
    print(python_file)
    # Do other stuff with the file. No need for closing the file, because of the with statement.

# Result 
# arr = [5, 2, 9, 5, 6]

# for index, value in enumerate(arr):
#     print(f'{index} : {value}')

# Result
# 0 : 1
# 1 : 2
# 2 : 4
# 3 : 5
# 4 : 6