import re
a=input()
b=input()
c=input()
d=input()
if re.match("kp{3,5}",a):
    print("VALID")
else:
    print("INVALID")

if re.match("[A-Z]+_[a-z]+",b):
    print("VALID")
else:
    print("INVALID")

if len(c)==5:
    if re.match("[0-9]",c):
        if re.match("\$",c[4]):
            print("VALID")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")

if len(d)==1:
    if re.match("[?*+]",d):
        print("VALID")
    else:
        print("INVALID")
else:
    print("INVALID")
                
