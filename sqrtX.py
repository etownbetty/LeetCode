class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #seems like a search - find the divisible number
        # unless the resulting divisible number is the same, keep binary searching
        if x ==0:
            return 0
        left = 1
        right = x
        while left<=right:
            mid = (left+right)//2
            if (mid > x//mid):
                print(mid, x//mid)
                right = mid-1
            elif (mid+1 > x//(mid+1)):
                print(mid+1, x//(mid+1))
                return mid
            else:
                left = mid+1
        
    def mySqrtNewton(self, x):
        r = x
        while r*r > x:
            # use reasonably good approximation, which is the number plus divisible number //2
            r = (r + x//r) // 2
        return r