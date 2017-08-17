class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []
        for p in sorted(people, key=lambda x: x[0], reverse=True):
            res.insert(p[1], p)
        return res


solution = Solution()
print(solution.reconstructQueue([[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
