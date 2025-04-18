from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for number in nums:
            if number < minNum:
                minNum = number
        return minNum
