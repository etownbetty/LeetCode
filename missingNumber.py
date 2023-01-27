# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        tot = int(len(nums)*(len(nums)+1)/2)
        while i<len(nums):
            tot-=nums[i]
            i+=1
        return tot