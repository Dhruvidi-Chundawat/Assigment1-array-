def min_max_element(arr1):
    minimum = arr1[0]
    maximum = arr1[0]
    
    for num in arr1:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
            
    return minimum, maximum

print(min_max_element([2, 9, 6, 1]))
