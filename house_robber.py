
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        just_robbed = current_rob = 0

        for house in nums:

        	#total of all robbed houses: algorithm is max(current+house(n-2) or house(n-1)), either rob (current+house(n-2)) or not rob the house (house(n-1))
        	total = max(house+current_rob, just_robbed)
        	#reset the house we are currently robbing
        	current_rob = just_robbed
        	#reset the house we just robbed
        	just_robbed = total

        return total 


# nums = [2,1,1,2]

# current_rob = 2, 1, 3, 4 
# just_robbed = 0, 2, 2, 3

# current_rob = 2
# just_robbed = 0

# current_rob = 1
# just_robbed = 2

# current_rob = 1+2
# just_robbed = 1

# current_rob = max(current_rob(n-1)=3, n+ 
# just_robbed = 3


# current_rob = n+just_robbed(n-1)
# algorithm is max(current_rob and just_robbed[n-1])