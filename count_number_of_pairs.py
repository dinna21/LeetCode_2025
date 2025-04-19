nums = [0,1,7,4,4,5]

#I used the bubble sort for sorting this array 
n = len(nums)
for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            swapped = True
    if(swapped == False):
        break
# print(nums)

minNum = nums[0]
maxNum = nums[n-1]
# print(maxNum)

OutDict = {}
lower = 3
upper = 6
n = len(nums)
count = 0
for i in range(n):
    # swapped = False
    # c =1
    for j in range(i+1,n):
        # c+=1
        # print(i)
        # print(j)
        print(nums[i]+nums[j])
        if(lower <= nums[i]+nums[j] <= upper):
            count+=1
print(count)

