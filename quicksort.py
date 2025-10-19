
def quick_sorted(arr):
    if len(arr)<=1:
        return arr
    
    lastElem=arr[-1]

    right = [j for j in arr[:-1] if j>lastElem]
    left = [j for j in arr[:-1] if j<=lastElem]

    return quick_sorted(left) + [lastElem] + quick_sorted(right)

arr=[45, 2, 11, 10, 3, 5, 77, 51]
print(arr)
print("sorted: ", quick_sorted(arr))