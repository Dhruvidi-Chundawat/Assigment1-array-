def rearrange_alternate(arr):
    arr.sort()
    result = []

    i = 0
    j = len(arr) - 1

    while i <= j:
        if i != j:
            result.append(arr[j])
            result.append(arr[i])
        else:
            result.append(arr[i])
        i += 1
        j -= 1

    return result


print(rearrange_alternate([1,2,3,4,5,6]))
