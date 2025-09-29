def linear_search(arr, target):
    for j in range(len(arr)):
        if arr[j] == target:
            return j
    return -1



arr = [1, 2, 3, 4, 22, 5, 7, 45, 88, 9, 11, 13]
target = int(input("Enter target num: "))
result = linear_search(arr, target)
print(result)  
