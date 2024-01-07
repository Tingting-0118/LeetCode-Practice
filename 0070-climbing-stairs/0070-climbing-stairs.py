class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 1:
        #     return 1
        # ways = [0] * (n+1)
        # ways[1] = 1
        # ways[2] = 2
        # for i in range(3,n+1):
        #     ways[i] = ways[i-1] + ways[i-2]
        # return ways[n]
        
        if n <= 2:
            return n
        ways1 = 1
        ways2 = 2
        current = 0
        for i in range(3, n+1):
            current = ways1 + ways2
            ways1 = ways2
            ways2 = current 
            
        return current 
            
    