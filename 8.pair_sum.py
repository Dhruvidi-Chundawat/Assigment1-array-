def pair_sum(arr, target):
    
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]

print(pair_sum([1,3,5,6], 7))            
