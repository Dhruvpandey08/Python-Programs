n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b,c,d=0,0,0
for i in a:
    if i>0:
        b=b+1
    if i<0:
        c=c+1
    if i==0:
        d=d+1
print(sum(a))
print(b)
print(c)
if d==0:
    print(-1)
else:
    print(d)
