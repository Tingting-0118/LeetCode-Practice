class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        strs.sort()
        first = strs[0]
        last = strs[-1]
        common_prefix = []
        for i in range(min(len(first),len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
                return ""
        result = "".join(common_prefix)
        return result 

