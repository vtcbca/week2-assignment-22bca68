# program to check prime number.
n=int(input("Enter a number :"))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not a prime number")
        else:
            print(n,"is a prime number")
