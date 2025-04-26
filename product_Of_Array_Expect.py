# Here is the Question 

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# Here Is the Solution That I made for THis Question 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        output = [1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        for i in range(n):
            output[i] = prefix[i]*suffix[i]
        return output
# And Here Is the Explanation Using ChatGpt


# Suppose your array is:
# nums = [1, 2, 4, 6]

# We want to find the output array where each position i has the product of all numbers except nums[i].

# Step 1: Think about the "prefix products"
# The prefix product at any index i is:
# product of all elements to the left of i.

# Before index 0: No elements → prefix = 1 (neutral for multiplication)

# Before index 1: Only nums[0] → prefix = 1

# Before index 2: nums[0] × nums[1] → 1 × 2 = 2

# Before index 3: nums[0] × nums[1] × nums[2] → 1 × 2 × 4 = 8

# Prefix array looks like this:

# Index	Prefix Product
# 0	1
# 1	1
# 2	2
# 3	8
# Step 2: Think about the "suffix products"
# The suffix product at any index i is:
# product of all elements to the right of i.

# After index 3: No elements → suffix = 1

# After index 2: Only nums[3] → suffix = 6

# After index 1: nums[2] × nums[3] → 4 × 6 = 24

# After index 0: nums[1] × nums[2] × nums[3] → 2 × 4 × 6 = 48

# Suffix array looks like this:

# Index	Suffix Product
# 0	48
# 1	24
# 2	6
# 3	1
# Step 3: Final Output
# Now, for each index i,
# you multiply prefix[i] × suffix[i].

# Index	Prefix[i]	Suffix[i]	Output[i] = Prefix[i] × Suffix[i]
# 0	1	48	48
# 1	1	24	24
# 2	2	6	12
# 3	8	1	8
# Thus,
# ✅ Final Output: [48, 24, 12, 8]