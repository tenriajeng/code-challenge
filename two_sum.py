def TwoSum(arr):
    target_sum = arr[0]  
    result_pairs = []  
    seen_numbers = set()
    
    for number in arr[1:]: 
        complement = target_sum - number 
        if complement in seen_numbers: 
            result_pairs.append(f"{complement},{number}")  
        seen_numbers.add(number)
    
    return ' '.join(result_pairs)

arr = [7, 3, 5, 2, -4, 8, 11]
print(TwoSum(arr))