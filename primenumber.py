n=int(input("enter a program to check wether the given number is perfect number or not:"))
lst=[]
for i in range(2,n):
    if n%i==0:
        print("the given number is not a prime number")
        break
else:
    print("the given number is a prime number")
