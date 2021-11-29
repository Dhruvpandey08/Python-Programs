n=int(input())
l=[]
a=[]
b=0
c=0
d=0
for i in range(n):
    e=input()
    l.append(e)
    a.append(e)
    for i in e:
        if e.isalpha():
            b=b+1
        if e.isdigit():
            c=c+1
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            d=d+1
            
print(tuple(l))
print("LETTERS",b)
print("DIGITS",c)
print("VOWELS",d)

print(len(l))
l.pop(0)
print(tuple(l))
print(tuple(a[0:3]))
print(a[-2])
print(a[-1]+"end")
print(a[0]*3)
print("12345" in l)
a.sort()
print(a)
