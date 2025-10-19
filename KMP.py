def failureFunction(P):
 m =  len(P)
 F = [0]*m
 j= 1
 i = 0  

 
 while j <  m:
  if P[j] == P[i]:
    i+=1
    F[j]=i
    j+=1
  elif i>0:
    i=F[i-1] 
  else:
    F[j] =0
    j+=1
 return F 
 
def KMPMatch(T, P):
 n=len(T) 
 m=len(P)
 i=0
 j=0
 F=failureFunction(P)

 while i <n:
  if T[i] == P[j]:
   if j==m-1:
    return i-j
   else:
    i+=1 
    j+=1
  elif j>0:
   j=F[j-1]  
  else:
   i+=1
 return -1   


T = "hgjgssggsgdjsdgjsdhgjsdgjsdjs"
P="sgdj"

result=KMPMatch(T, P)
print("found at index: ", result )