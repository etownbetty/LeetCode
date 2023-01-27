class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #make output, set first pointer
        trips, i  = [], 0
        #sort nums to find the triples
        nums.sort()

        while i<len(nums)-2:
            #set j and k, j is 1 spot after i, k is at the end of the list
            j,k = i+1,len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    #add to result and check for other same solutions
                    trips.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
        return trips