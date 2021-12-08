def calcDA(DA1,DA2,DA3):
    output = DA1+DA2+DA3 
    return output

def calcCAT(CAT1,CAT2):
    output = ((CAT1/30)*15) + ((CAT2/30)*15)
    return output

def calcFAT(marks):
    output = marks*0.4
    return output

def calcTOTAL(DA,CAT,FAT):
    output = DA+CAT+FAT
    return output

n=int(input())

output=[]

for i in range(n):
    DA=[]
    for i in range(3):
        DA.append(int(input()))
    CAT=[]
    for i in range(2):
        CAT.append(int(input()))
    FAT=int(input())

    weight_DA = calcDA(DA[0],DA[1],DA[2])
    weight_CAT = calcCAT(CAT[0],CAT[1])
    weight_FAT = calcFAT(FAT)

    weight_total = calcTOTAL(weight_DA,weight_CAT,weight_FAT)

    output.append(weight_total)

print(output)


