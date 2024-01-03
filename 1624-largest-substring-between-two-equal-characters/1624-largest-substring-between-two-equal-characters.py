class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_occurance = {}
        max_length = -1
        for i, char in enumerate(s):
            if char in first_occurance:
                current_length = i - first_occurance[char] - 1
                max_length = max(max_length, current_length)
            else:
                first_occurance[char] = i

        return max_length


            