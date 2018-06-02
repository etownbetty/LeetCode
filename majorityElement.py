class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if d.get(i) is not None:
                d[i] += 1
            else:
                d[i] = 1
        return max(d, key=d.get)

        #O(n) time, have to go through the array once to add up the elements - actually O(n)+O(m), where m is the number of different elements

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]    
        # O(nLogn) time, the cost of sorting the array    
                