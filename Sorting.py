#Taking list as an input from the user
l = []
n = int(input())
for i in range (1, n+1, 1):
    element = int(input())
    l.append(element)
print(l)
#Checking if the elemnt is present in the list.
a = int(input("Enter the no to be searched"))
flag = 0
for j in range (0, n, 1):
    if l[j] == a:
        flag = flag + 1
print("Index: ",j+1)
if flag > 0:
    print("It is present")
else:
    print("It is not present")