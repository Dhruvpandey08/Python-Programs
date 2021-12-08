def findsec(a):
    c=True
    b=str(a)
    
    for i in range(len(b)):
        if b[i] != b[len(b)-int(i)-1]:
            c=False
            
    return(c)
    
n=int(input())

d = []

for i in range(n):
    data=int(input())
    if len(str(data)) !=5:
        print("invalid entry")
        exit()
    else:
        d.append(data)
        
for i in d:
    if findsec(i):
        print(i)
