class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #implement binary search for needle in haystack
        i = 0
        while (i+len(needle))<=len(haystack):
            #look at the beginning of haystack
            if haystack[i:i+len(needle)]==needle:
                return i
            else:
                i+=1
        return -1