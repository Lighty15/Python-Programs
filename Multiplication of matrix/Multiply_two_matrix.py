#Multiplication of two matrices

X=[[2,3,4],[4,2,3],[3,5,4]]
Y=[[3,2,1],[1,4,2],[2,4,1]]
Result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            Result[i][j]+=X[i][k]*Y[k][i]

print("Matrix X:",X)
print("Matrix Y:",Y)
print("Multiplication of matrices X and Y:")

for r in Result:
    print(r)
