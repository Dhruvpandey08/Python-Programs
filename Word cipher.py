s=input()
s1=''       #to avoid junk
for i in s:
    n=ord(i)+3  #ASCII
    if n>ord('z'):
        n=ord('a')+(n-122)-1
    c1=chr(n)
    s1=s1+c1
print(s1)
