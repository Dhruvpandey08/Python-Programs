s=input()
vowel=0
newstr=s
vowels="aeiou"
for i in s.lower():
    if i in vowels:
        newstr=newstr.replace(i,chr(ord(i)+1))
        vowel+=1
print(newstr)
print(vowel)
