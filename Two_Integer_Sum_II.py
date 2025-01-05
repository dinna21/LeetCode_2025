numbers = [-3,3,4,90]
target = 0
nums = []

if target == 0:
    # Use enumerate to iterate with indices
    for i, num in enumerate(numbers):
        if num == 0:
            nums.append(i + 1)  # Append the 1-based index
        else:
            seen = []
            if -num in seen:
                nums.append(i + 1) # Append the 1-based index
            seen.append(num)

            


else:
    # Iterate through the array with indices
    for i, num in enumerate(numbers):
        complement = target - num

        # Check for complement in the array
        for j in range(len(numbers)):
            if i != j and numbers[j] == complement:
                nums.append(i + 1)  # Append 1-based index of `num`
                nums.append(j + 1)  # Append 1-based index of `complement`
                break

        if nums:  # Break the outer loop if a pair is found
            break

print(nums)
# def twoSum1(self, numbers, target):
#     l, r = 0, len(numbers)-1
#     while l < r:
#         s = numbers[l] + numbers[r]
#         if s == target:
#             return [l+1, r+1]
#         elif s < target:
#             l += 1
#         else:
#             r -= 1
 
# # dictionary           
# def twoSum2(self, numbers, target):
#     dic = {}
#     for i, num in enumerate(numbers):
#         if target-num in dic:
#             return [dic[target-num]+1, i+1]
#         dic[num] = i
 
# # binary search        
# def twoSum(self, numbers, target):
#     for i in xrange(len(numbers)):
#         l, r = i+1, len(numbers)-1
#         tmp = target - numbers[i]
#         while l <= r:
#             mid = l + (r-l)//2
#             if numbers[mid] == tmp:
#                 return [i+1, mid+1]
#             elif numbers[mid] < tmp:
#                 l = mid+1
#             else:
#                 r = mid-1