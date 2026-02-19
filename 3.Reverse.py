def reverse_arr(arr1):
    rev_arr = []
    while arr1:
        rev_arr.append(arr1.pop())
    return rev_arr

print(reverse_arr([4, 3, 6, 7]))
