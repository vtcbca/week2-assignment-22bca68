# program to check palindrom number
n=int(input("enter a number to be checked:"))
reverse=0
c=n
while(n!=0):
    remainder=n%10
    reverse=reverse*10+remainder
    n//=10
if c==reverse:
    print("{} is a palindrome number".format(c))
else:
    print("{} is not a palindrome number".format(c))
