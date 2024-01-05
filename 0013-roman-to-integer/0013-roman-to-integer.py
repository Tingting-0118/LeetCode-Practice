class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and symbol_value[s[i]] < symbol_value[s[i+1]]:
                total += (symbol_value[s[i+1]] - symbol_value[s[i]])
                i = i +2
            
            else:
                total += symbol_value[s[i]]
                i = i + 1
        return total 