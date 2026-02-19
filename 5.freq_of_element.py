def freq_of_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
print(freq_of_element([1,3,1,1,4,5,2,3,4]))
    