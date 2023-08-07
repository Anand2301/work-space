def great(arr,n):
    for i in range(n-1):
        s=len(arr)
        arr.sort()
    return(arr[s-n])
great([12,67,87,90,34,12,3,56],4)
