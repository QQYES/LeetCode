from math import floor


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        while n > 0:
            count = 0
            i = int(floor(n ** 0.5))
            while i > 0:
                n -= i ** 2
                count += 1
                i = int(floor(n ** 0.5))


solution = Solution()
print(solution.numSquares(12))
