s=input()
alphabets="abcdefghijklmnopqrstuvwxyz"
check=True
for i in alphabets:
    if i not in s:
        check=False
        break
if check==True:
    print("pangram")
else:
    print("not pangram")
