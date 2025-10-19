def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2

    return arr


x= [7, 12, 34, 10,6, 54, 2, 3, 88, 11, 1, 45,17]
print("before:", x)
shellSort(x)
print("after:", x)
