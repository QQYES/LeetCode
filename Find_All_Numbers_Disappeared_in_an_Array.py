class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [i for i in range(min(nums), max(nums) + 1)]
        for num in nums:
            if num in res:
                res.remove(num)
        return res


solution = Solution()
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 3, 3, 1]))
