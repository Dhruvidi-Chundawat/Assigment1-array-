def common_element(arr1, arr2):
     result = []
     for num in arr1:
          if num in arr2:
               result.append(num)
     return result            
   # for i in range(len(arr1)):
        #for j in range(len(arr2)):
         #   if arr1[i] == arr2[j]:
          #      return arr1[i]
print(common_element([1,2,3,4], [4,5,1,8]))            