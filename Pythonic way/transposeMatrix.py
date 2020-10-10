x = [[31,17],
[40 ,51],
[13 ,12]]
    
t=list(zip(*x))
# convert list of tuples to list of list 
res = [list(ele) for ele in t]
print(res)


# Result
# [[31, 40, 13], [17, 51, 12]]