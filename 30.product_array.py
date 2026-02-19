def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result


print(product_except_self([1,2,3,4]))
