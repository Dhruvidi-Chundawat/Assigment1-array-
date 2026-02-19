def max_product_pair(arr):
    arr.sort()

    n = len(arr)

    product1 = arr[n-1] * arr[n-2]
    product2 = arr[0] * arr[1]

    if product1 > product2:
        return (arr[n-2], arr[n-1])
    else:
        return (arr[0], arr[1])


print(max_product_pair([-10,-3,5,6]))
