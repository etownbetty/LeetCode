#Given an array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #put the nums in a dict, then iterate through dict to find which one has a value ==1
        dnums = {}
        for num in nums:
            if dnums.get(num)==None:
                dnums[num]=0
            dnums[num]+=1
        for k,v in dnums.items():
            if v==1:
                return k

    def singleNumber1(self, nums):
        return 2*sum(set(nums))-sum(nums)