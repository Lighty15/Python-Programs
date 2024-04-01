#Adding two matrix

A=[[2,3,4],[3,4,6],[4,2,5]]
B=[[3,2,6],[2,1,4],[1,4,2]]
Result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]=A[i][j]+B[i][j]

print("Matrix A:",A)
print("Matrix B:",B)
print("Addition of matrix A & B:",)

for r in Result:
    print(r)
