a=int(input())
b=int(input())

#check for square matrix, print invalid if matrix is not a square matrix

if a!=b:
    print("Invalid")
    exit()

A=[]

#Return the largest number in the list
def maximum(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i]<lst[i+1]:
                lst[i,lst][i+1]=lst[i+1],lst[i]
    return lst[0]

#Return the smallest number in the list
def minimum(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i]<lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst[-1]

for i in range(a):
    temp=[]
    for j in range(b):
        temp.append(int(input()))
    A.append(temp)

#Largest element of leading diagonal elements
print(A[a-1][b-1])
A[a-1].pop(b-1)

print(A[0][b-1])
A[0].pop(b-1)

max=0
for i in A:
    for j in i:
        if j>max:
            max=j
print(max)