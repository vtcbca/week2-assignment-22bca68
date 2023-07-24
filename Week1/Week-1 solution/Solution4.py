# program to check whether number is armstrong number or not
num=int(input("Enter a number to be checked:"))
result=0
c=num
for i in range(num):
     if num!=0:
         r=num%10
         result+=r*r*r
         num//=10
if result==c:
     print("{} is a armstrong number".format(c))
else:
    print("{} is not a armstrong number".format(c))
