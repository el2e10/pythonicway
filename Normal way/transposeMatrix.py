M = 3
N = 2 

A = [[31,17],
[40 ,51],
[13 ,12]]
  
# To store result 
B = [[0 for x in range(M)] for y in range(N)]  

for i in range(N): 
    for j in range(M): 
        B[i][j] = A[j][i]
print(B)


# Result 
# [[31, 40, 13], [17, 51, 12]]