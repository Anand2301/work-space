for i in range(len(arr)):
min_index = i
for j in range(i, len(arr)):
if arr[j] < arr[min_index]: 
min_index = j 
arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)
