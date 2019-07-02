from itertools import product
a,b = map(str,input().split(","))
g1= int(input())
a = a.upper()
g2 = int(input())
b = b.upper()
gt = g1+g2
if gt ==0:
    print ("0")
    exit()
vet=list(a+b)
vet2 = product(vet, repeat=gt)
vet3=list(set(vet2))
vet3.sort()
for i in vet3:
    if i.count(a) == g1 and i.count(b) == g2:
        print(''.join(map(str, i)))
