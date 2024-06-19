num = int(input("enter the no. whose sum of digits is to be calculated: "))
sum=0
while(num!=0):
 dig1= num%10
 sum =sum+dig1
 num = num//10
print(sum)