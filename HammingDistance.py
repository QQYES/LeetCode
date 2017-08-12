class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str_x = '{:b}'.format(x)
        str_y = '{:b}'.format(y)
        max_len = max(str_x.__len__(), str_y.__len__())
        str_x = ('{:0>' + str(max_len) + '}').format(str_x)
        str_y = ('{:0>' + str(max_len) + '}').format(str_y)

        count = 0
        for i in range(str_x.__len__()):
            if str_x[i] != str_y[i]:
                count += 1

        return count


solution = Solution()
result = solution.hammingDistance(1, 4)
print result
