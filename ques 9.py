str = input("enter the string: ")
substr= input("enter the substring to be checked: ")
result= substr in str
if (result):
    print("yes the given substring is present in the string")
else:
    print("the given substring is not present in the string")