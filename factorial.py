fa=int(input("enter the number to find its factorial:"))
factorial=1
if fa<0:
    print("invalid number")
elif fa==0:
    print("invalid number")
else:
    for i in range(1,fa+1):
        factorial=factorial*i
print(factorial)
        
