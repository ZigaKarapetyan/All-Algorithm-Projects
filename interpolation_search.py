def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1



arr = [1, 3, 5, 4, 7, 9, 11, 13, 2]
arr.sort()
target = int(input("enter target num: "))
print(interpolation_search(arr, target)) 
