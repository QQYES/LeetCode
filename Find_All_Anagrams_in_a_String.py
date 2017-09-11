class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from itertools import permutations
        res = []
        p_com = [item for item in permutations(p)]
        p_len = len(p)
        for i in range(len(s)):
            if tuple(s[i:i + p_len]) in p_com:
                res.append(i)
        return res


solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))
