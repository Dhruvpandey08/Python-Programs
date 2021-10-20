m=int(input())
n=int(input())
c=0
for i in range(1,31):
    if i%m==0 and i%n==0:
        c+=1
        
print(c+1)
