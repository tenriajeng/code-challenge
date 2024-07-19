def binary_search(arr, target): 
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  
        mid_value = arr[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = binary_search(sorted_list, target)
print(f"Index of {target}: {index}")  
