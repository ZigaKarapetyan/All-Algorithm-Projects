def last_occ(P):
    L={}
    for i in range(len(P)):
        L[P[i]]=i
    return L 


def BoyerMoore(T, P):
    n=len(T)
    m=len(P)
    L= last_occ(P)
    i=0
    while i <= n-m:
        j=m-1
        while j >=0 and T[i+j] == P[j]:
            j-=1
        if j==-1:
          print("found at index", i)
          return i
        else:
            last=L.get(T[i+j], -1)
            i=i+max(1,j-last)
    print("not found")        
    return -1


T = "hgjgssggsgdjsdgjsdhgjsdgjsdjs"
P="sgdj"
BoyerMoore(T,P)


