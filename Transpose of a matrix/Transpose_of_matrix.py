#Transpose of a Matrix

A=[[2,3],[4,5],[6,7]]
Result=[[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        Result[j][i]=A[i][j]
        
print("Matrix A:", A)
print("Transpose of Matrix A:")

for r in Result:
    print(r)
