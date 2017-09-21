class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        left = 0
        right = 0
        s_res = sorted(nums)
        if s_res == nums:
            return 0
        for i in range(len(nums)):
            if s_res[i] != nums[i]:
                left = i
                break
        for j in range(len(nums) - 1, 0, -1):
            if s_res[j] != nums[j]:
                right = j
                break
        return right - left + 1
        # print(nums)
        # print(s_res)


s = Solution()
print(s.findUnsortedSubarray([1, 2]))
