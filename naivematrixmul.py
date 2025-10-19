def matrixMul(A,B):
 n=len(A)
 C=[]
 for i in range(n):
  row=[]
  for j in range(n):
   val=0
   for k in range(n):
    val=val + A[i][k]*B[k][j]
   row.append(val)
  C.append(row)
 return C

A=[[11,22],[13,55]]
B=[[10,9],[12,6]]
print("result:")
print(matrixMul(A,B))
