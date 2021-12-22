a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
b=int(input())
c=set(a)
print(a.count(b))
print(len(c))