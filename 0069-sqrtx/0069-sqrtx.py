class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            middle = (left + right)//2
            square = middle * middle
            if square == x:
                return middle
            elif square < x:
                left = middle + 1
            else: 
                right = middle - 1
        return right 
            