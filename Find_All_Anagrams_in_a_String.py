class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_set = set(p)
        p_len = len(p)
        for i in range(len(s)):
            if len(s[i:i + p_len]) == p_len and len(p_set) == len(set(s[i:i + p_len])) and p_set == set(s[i:i + p_len]):
                res.append(i)
        return res


solution = Solution()
print(solution.findAnagrams("ababababab", "aab"))
