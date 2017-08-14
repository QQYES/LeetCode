class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up_count = 0
        lr_count = 0
        for move in moves:
            if move == 'U':
                up_count += 1
            if move == 'D':
                up_count -= 1
            if move == 'L':
                lr_count += 1
            if move == 'R':
                lr_count -= 1

        if up_count == 0 and lr_count == 0:
            return True
        else:
            return False



solution = Solution()
print(solution.judgeCircle("UD"))