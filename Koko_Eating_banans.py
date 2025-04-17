import math
piles = [1,4,3,2]
ksValues = []
h=9
k = 1

while(k<=max(piles)):
    temp = []
    for pile in piles:
        result = math.ceil(pile/k)
        temp.append(result)
        # print(k)
    ksValues.append((k,sum(temp)))
    k+=1
print(ksValues)


for val in ksValues:
    if val[1] <=h:
        print(val[0])
        break