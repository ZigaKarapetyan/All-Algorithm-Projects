def ternary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1


arr = [1, 2, 3, 4, 22, 5, 7, 45, 88, 9, 11, 13, 8 , 9, 12]
arr.sort()
target = int(input("enter target num: "))
print(ternary_search(arr, target))  
