from functools import reduce


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_num = nums.count(0)
        if zero_num > 1:
            return [0] * len(nums)
        if zero_num == 1:
            res = [0] * len(nums)
            zero_index = nums.index(0)
            nums.remove(0)
            res[zero_index] = reduce(lambda x, y: x * y, nums)
            return res
        if zero_num == 0:
            sums = reduce(lambda x, y: x * y, nums)
            return list(map(lambda x: sums / x, nums))


s = Solution()
print(s.productExceptSelf([1, 0]))
