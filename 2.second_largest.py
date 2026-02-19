def second_largest(arr1):
    if len(arr1) < 2:
        return None

    first = second = float('-inf')

    for num in arr1:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num

    return second


print(second_largest([2, 9, 6, 1]))
