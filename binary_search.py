def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



arr = [1, 2, 3, 4, 22, 5, 7, 45, 88, 9, 11, 13, 8 , 9, 12]
arr.sort()
target = int(input("Enter target num: "))
result = binary_search(arr, target)
print(result)
