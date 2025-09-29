import math
def jump_search(arr, target):
    n= len(arr)
    m=int(math.sqrt(n))
    prev=0
    while prev <n and arr[min(m, n) -1]< target:
        prev=m
        m+=int(math.sqrt(n))
        if prev >= n:
            return -1
        
    while prev < n and arr[prev] < target:
        prev+=1

    if prev <n and arr[prev] == target:
        return prev
    return -1        
  
arr = [15, 45, 23, 56, 88, 9, 10, 11, 2]
arr.sort()
target = int(input("enter target num: "))
print("target found at: ", jump_search(arr, target))
