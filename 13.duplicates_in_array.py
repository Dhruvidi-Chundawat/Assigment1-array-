def duplicates(arr):
    check = {}
    result = []
    for num in arr:
        check[num] = check.get(num, 0) +1
    for num, count in check.items():
        if count > 1:
            result.append(num)  
    return result
print(duplicates([1,3,2,2,4,5,1]))          