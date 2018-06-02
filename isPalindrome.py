class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x)
        left = 0
        right = len(xstr)-1
        while left<=right:
            if xstr[left]!=xstr[right]:
                return False
            left+=1
            right-=1
        return True