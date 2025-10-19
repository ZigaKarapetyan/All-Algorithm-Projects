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



arr=["apple","banana","cherry","grape","orange","peach"]
target="grape"
arr.sort()
result = binary_search(arr, target)
print(result)