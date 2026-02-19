def max_difference(arr):
    min_so_far = arr[0]
    max_diff = 0

    for j in range(1, len(arr)):
        diff = arr[j] - min_so_far
        max_diff = max(max_diff, diff)
        min_so_far = min(min_so_far, arr[j])

    return max_diff


print(max_difference([2,3,10,6,4,8,1]))
