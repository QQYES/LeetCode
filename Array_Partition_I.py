class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(sorted(nums)[::2])


solution = Solution()
print(solution.arrayPairSum([1, 4, 3, 2]))
