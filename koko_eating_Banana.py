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
# THis is the first code I implement I lost this cause of github cli issue 
import math

piles = [1, 4, 3, 2]
ksValues = []
h = 9
k = 1

while k <= max(piles):  # include max(piles)
    temp = []
    for pile in piles:
        result = math.ceil(pile / k)
        temp.append(result)
    ksValues.append((k, sum(temp)))  # store k and total hours
    k += 1

# Print all k and total hours it would take
for val in ksValues:
    print(f"k={val[0]}, total_hours={val[1]}")

# Find the minimum k with total_hours <= h
for val in ksValues:
    if val[1] <= h:
        print(f"\n✅ Minimum k to eat all bananas in {h} hours is: {val[0]}")
        break
# /////////////////This is correted code for above scenario 


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [1,4,3,2]
        ksValues = []
        # h=9

        k = 1
        while(k<=max(piles)):
            temp = []
            for pile in piles:
                result = math.ceil(pile/k)
                temp.append(result)
                # print(k)
            ksValues.append((k,sum(temp)))
            k+=1
        # print(ksValues)


        for val in ksValues:
            if val[1] <=h:
                return (val[0])
                break
        