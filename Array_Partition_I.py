class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        sub_nums = []
        i = 0
        for num in nums:
            if (i % 2) == 0:
                sub_nums.append(num)
            i = i + 1
        return reduce(lambda x, y: x + y, sub_nums)


solution = Solution()
print(solution.arrayPairSum([1, 4, 3, 2]))
