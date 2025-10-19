def add_matrix(A,B):
 n=len(A)
 C = [[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):
   C[i][j] = A[i][j]+B[i][j]
 return C

def sub_matrix(A,B):
 n =len(A)
 C = [[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):
   C[i][j] = A[i][j]-B[i][j]
 return C

def strassen(A,B):
 n = len(A)
 if n == 1:
  return [[A[0][0]*B[0][0]]]
 mid = n//2

 A11=[row[:mid] for row in A[:mid]]
 A12=[row[mid:] for row in A[:mid]]
 A21=[row[:mid] for row in A[mid:]]
 A22=[row[mid:] for row in A[mid:]]
 B11=[row[:mid] for row in B[:mid]]
 B12=[row[mid:] for row in B[:mid]]
 B21=[row[:mid] for row in B[mid:]]
 B22=[row[mid:] for row in B[mid:]] 

 M1=strassen(add_matrix(A11,A22),add_matrix(B11,B22))
 M2=strassen(add_matrix(A21,A22),B11)
 M3=strassen(A11,sub_matrix(B12,B22))
 M4=strassen(A22,sub_matrix(B21,B11))
 M5=strassen(add_matrix(A11,A12),B22)
 M6=strassen(sub_matrix(A21,A11),add_matrix(B11,B12))
 M7=strassen(sub_matrix(A12,A22),add_matrix(B21,B22))

 C11 =  add_matrix(sub_matrix(add_matrix(M1,M4),M5),M7)
 C12 = add_matrix(M3,M5)
 C21 =add_matrix(M2,M4)
 C22 = add_matrix(sub_matrix(add_matrix(M1,M3),M2),M6)

 newM=[[0]*n for _ in range(n)]
 for i in range(mid):
  for j in range(mid):
   newM[i][j] = C11[i][j]
   newM[i][j+mid] = C12[i][j]
   newM[i+mid][j] = C21[i][j]
   newM[i+mid][j+mid] = C22[i][j]
 return newM

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print("Result:")
print(strassen(A,B))
