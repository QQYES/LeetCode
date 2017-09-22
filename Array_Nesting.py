class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}
        for i in range(len(nums)):
            s = set()
            s.add(nums[i])
            begin = i
            while i != nums[begin]:
                begin = nums[begin]
                if begin in mem.keys():
                    mem.setdefault(i, len(s) + mem.get(begin))
                    break
                s.add(nums[begin])
            if i in mem.keys():
                pass
            else:
                mem.setdefault(i, len(s))
        return max(mem, key=mem.get)


solution = Solution()
print(solution.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
