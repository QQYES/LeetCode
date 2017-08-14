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
                    if index_in == 0 or index_in == len(sublist) - 1:
                        count += 1
                    else:
                        if sublist[index_in - 1] == 0:
                            count += 1
                        if sublist[index_in + 1] == 0:
                            count += 1

                    if index_out == 0 or index_out == len(grid) - 1:
                        count += 1
                    else:
                        if grid[index_out - 1][index_in] == 0:
                            count += 1
                        if grid[index_out + 1][index_in] == 0:
                            count += 1

        return count


solution = Solution()
print(solution.islandPerimeter([[0, 1, 0, 0],
                                [1, 1, 1, 0],
                                [0, 1, 0, 0],
                                [1, 1, 0, 0]]))
