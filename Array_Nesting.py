class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}
        for i in range(len(nums)):
            if i in mem.keys():
                continue
            s = set()
            s.add(nums[i])
            begin = i
            while i != nums[begin]:
                begin = nums[begin]
                s.add(nums[begin])
            if i in mem.keys():
                pass
            else:
                mem.setdefault(i, len(s))
        return max(mem.items(), key=lambda d: d[1])[1]


solution = Solution()
print(solution.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
