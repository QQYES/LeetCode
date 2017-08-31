from math import floor


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for index in range(1, n + 1):
            if index == 1:
                dp[index] = 1
            else:
                for i in range(1, index + 1):
                    num = index
                    while num>0:
                        count = 0
                        i += i ** 2
                        count += 1
                        if i == index:


solution = Solution()
print(solution.numSquares(12))
