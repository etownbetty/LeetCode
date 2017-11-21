class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split())>0:
            return len(s.split()[-1])
        else:
            return 0