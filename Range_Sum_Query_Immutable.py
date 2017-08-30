class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        sums = 0
        for index, num in enumerate(nums):
            self.dp[index] =

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
i = 0
j = 2
param_1 = obj.sumRange(i, j)
print(param_1)
