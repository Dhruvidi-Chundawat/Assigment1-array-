def if_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    
    return True
print(if_sorted([2, 3, 5, 9]))     