lines=[]
while True:
    i=input()
    if i:
       lines.append(i.upper())
    else:
        break
    for r in lines:
        print(r)