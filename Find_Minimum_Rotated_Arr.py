from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for number in nums:
            if number < minNum:
                minNum = number
        return minNum
    def findMin(self, Binarynums: List[int]) -> int:
        left=0,right = len(Binarynums)-1
        while left < right:
            mid = (left+right)//2
            if Binarynums[mid] > Binarynums[right]:
                left = mid+1
            else:
                right = mid
        return Binarynums[left]
