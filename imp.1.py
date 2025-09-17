A=[[1,2,3],
   [4,5,6]]
B=[[2,2],
   [2,2],
   [2,2]]
result=[[0 for _ in range (len(B[0]))] for _ in range(len(A))]
for i in range (len(A)):
    for j in range (len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
print("Result of matrix multiplication:")
for row in result:
    print (row)