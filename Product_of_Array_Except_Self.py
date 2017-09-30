from functools import reduce


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if isinstance(nums, list):
            zero_num = nums.count(0)
            if zero_num > 1:
                return [0] * len(nums)
            if zero_num == 1:
                sums = reduce(lambda x, y: x * y, list(nums.))
                res = []
                for item in nums:
                    if item != 0:
                        res.append(0)
                    else:
                        res.append(sums)
                return res
            if zero_num == 0:
                sums = reduce(lambda x, y: x * y, nums)
                res = []
                for item in nums:
                    if item != 0:
                        res.append(sums / item)
                    else:
                        res.append(sums)
                return res


s = Solution()
print(s.productExceptSelf([1, 0]))
