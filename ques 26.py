str = input("enter the string: ")
suffix=input("enter the suffix to be checked: ")
prefix=input("enter the prefix to be checked: ")
if str.startswith(prefix):
    print("the string starts with the given prefix!")
if str.endswith(suffix):
    print("the string starts with the given suffix!")