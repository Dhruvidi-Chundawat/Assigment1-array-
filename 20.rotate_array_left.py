def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

print(rotate_left([1,2,3,4,5], 2))
