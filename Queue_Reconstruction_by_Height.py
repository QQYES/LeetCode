class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if isinstance(people, list):
            tmp = sorted(people, key=lambda x: (-x[0], x[1]))
            print(tmp)

        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)
        return res


solution = Solution()
solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
