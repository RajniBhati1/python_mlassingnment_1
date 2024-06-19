n=int(input("enter n: "))
a=0
b=1
i=1
print(a,b , end=" ")#using end so that next print statement continues from the same line
while (i<(n-1)):
 c=a+b
 print(c, end=" ")
 i=i+1
 a=b
 b=c

