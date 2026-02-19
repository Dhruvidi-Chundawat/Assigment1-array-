def remove_element(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            arr.pop(i)
        else:
            i += 1
    return arr

print(remove_element([1,2,3,4,1], 1))
