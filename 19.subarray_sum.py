def subarray_sum(nums, target):
    result = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        
        if current_sum - target in result:
            return [result[current_sum - target] + 1, i]
        
        result[current_sum] = i
    
    return result


print(subarray_sum([1,2,3,4,5,6], 10))
