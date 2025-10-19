def binarySearch(arr, left, right, x):
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return -1

def exponentialSearch(arr, x):
    n = len(arr)
    if arr[0]== x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i*2
    return binarySearch(arr, i//2, min(i, n-1), x)


arr = [11, 45, 87, 88, 100 ,2, 26,3, 4, 77,10, 40,55, 70]
arr.sort()
x = 77
result = exponentialSearch(arr, x)
if result != -1:
    print("found at index:", result)
else:
    print("not found")
