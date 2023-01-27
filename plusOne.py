class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        i = len(digits)-1
        for digit in digits:
            #convert to number, add 1, then convert to list
            num += digit*(10**i)
            i-=1
        return [int(i) for i in str(num+1)]