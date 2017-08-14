class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count = 0
        for index_out, sublist in enumerate(grid):
            for index_in, elem in enumerate(sublist):
                if elem:
                    if elem[index_in - 1] == 0:
                        count += 1
                    if elem[index_in + 1] == 0:
                        count += 1

                    if index_out == 1 or index_out == len(grid):
                        count += 1

        return count


solution = Solution()
print(solution.islandPerimeter([[0, 1, 0, 0],
                                [1, 1, 1, 0],
                                [0, 1, 0, 0],
                                [1, 1, 0, 0]]))
