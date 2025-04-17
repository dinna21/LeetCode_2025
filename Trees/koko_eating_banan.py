piles = [1,4,3,2]
ksValues = []
h=9
k = 1
while(k<max(piles)):
    for pile in piles:
        result = int(pile/k)
        ksValues.append(result)
        # print(k)
    k+=1
print(ksValues)
created_arr = []
i = 0
while i<len(ksValues):
    created_arr.append(ksValues[i:i+4])
    i+=4

print(created_arr)

for nums in created_arr:
    if(sum(nums) == h or sum(nums) < h):
        print(sum(nums))
    else:
        print(0)