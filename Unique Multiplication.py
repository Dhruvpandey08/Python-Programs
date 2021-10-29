md=int(input())
mr=int(input())
multiply=md*mr
mds=str(md)
mrs=str(mr)
multiplys=str(multiply)
c=0
for i in (multiplys):
    for j in (mds):
        for k in (mrs):
            if k==j or j==i or i==k:
                c+=1
if c!=0:
    print("No")
else:
    print("Yes")