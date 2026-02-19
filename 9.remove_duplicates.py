def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

print(remove_duplicates([1,3,4,2,1,1,5]))
