class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i<len(nums):
            if nums[i]==val:
                #put it at the back of the array
                nums[i] = nums[n-1]
                #pop it off the back
                nums.pop()
                #set n as the new array length
                n = len(nums)
            else:
                i+=1
        return len(nums)