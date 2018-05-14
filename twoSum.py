### find the indices of the two numbers that make up the target
### there will be only one correct result each time

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comps = {}
        i = 0
        while i<len(nums):
            comp = target-nums[i]
            if comp in comps.keys():
                return [comps[comp], i]
            else:
                comps[nums[i]] = i
                i+=1