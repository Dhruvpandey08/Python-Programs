def count(n):
    c=0
    while(n):
        n=n&(n-1)
        c+=1
    if (c%2==0):
        return 1
    else:
        return 0

def sum_of_digits(n):
    sum=0
    while (n!=0):
        sum+=n%10
        n//=10
    return sum

b=int(input())
arr=[]
for i in range(b):
    arr.append(int(input()))
n=len(arr)
t_sum=0

for i in range(n):
    if(count(arr[i])):
        t_sum+=sum_of_digits(arr[i])
print(t_sum)
