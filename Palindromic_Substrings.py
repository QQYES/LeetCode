class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for center in range(2 * n - 1):
            left = int(center / 2)
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


solution = Solution()
print(solution.countSubstrings('abc'))
