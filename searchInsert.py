class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        while first<=len(nums)-1:
            if nums[first]==target:
                return first
            else:
                if target>nums[first]:
                    first+=1
                elif target<nums[first]:
                    return first
        return len(nums)

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """       
    return len([x for x in nums if x<target])