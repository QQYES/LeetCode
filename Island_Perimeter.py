class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if isinstance(grid, list):
            count = 0
            for index_out, sublist in enumerate(grid):
                for index_in, elem in enumerate(sublist):
                    if elem:
                        if elem[index_in - 1] == 0:

                            if index_out == 1 or index_out == len(grid):
