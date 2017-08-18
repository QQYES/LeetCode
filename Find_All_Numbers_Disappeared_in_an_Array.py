class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
            res = [i for i in range(1, len(nums) + 1)]
            return list(set(res) - set(nums))
        else:
            return []


solution = Solution()
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
