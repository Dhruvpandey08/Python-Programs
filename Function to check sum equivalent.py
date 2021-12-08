n=int(input())
l=[]
for i in range(n):
    d=int(input())
    l.append(d)
def check(d):
    a=[]
    for i in range(len(d)):
        b=0
        for j in str(d[i]):
            b=b+int(j)
        a.append(b)
    d=0
    for i in range(len(a)):
        if a[0]==a[i] and i!=0:
            d=d+1
    if d>=1:
        print(l[0])
        for i in range(len(a)):
            if a[0]==a[i] and i!=0:
                print(l[i])
                
    elif d==0:
        print("No sum-equivalent")
        
check(l)
