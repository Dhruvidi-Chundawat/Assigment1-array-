def missing_element(arr, n):
    expected_sum = n*(n+1)//2
    actual_sum = sum(arr)
    missing = expected_sum - actual_sum
    return missing
print(missing_element([1,2,3,4,6], 6))
