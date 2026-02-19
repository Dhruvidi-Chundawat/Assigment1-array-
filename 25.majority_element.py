def majority_element(arr):
    freq = {}
    n = len(arr)

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n//2:
            return num

    return -1


print(majority_element([2,2,1,1,2,2,2]))
