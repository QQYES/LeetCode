class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        s_res = sorted(nums)
        for i in range(len(nums)):
            if s_res[i] != nums[i]:
                left = i
                break
        for j in range(len(nums) - 1, 0, -1):
            if s_res[i] != nums[i]:
                right = j
                break
        return right - left
        # print(nums)
        # print(s_res)


s = Solution()
print(s.findUnsortedSubarray([2, 1]))
