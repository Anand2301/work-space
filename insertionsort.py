for i in range(len(arr)):
for j in range(i 1, -1, -1):
if arr[j] = arr[j+1]: 
arr[j], arr[j+1] = arr[j+1], arr[j]
else:
break
print(arr)
