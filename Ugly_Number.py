from sympy import factor


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 1:
            while num > 1:
                if num % 2 == 0:
                    num /= 2
                elif num % 3 == 0:
                    num /= 3
                elif num % 5 == 0:
                    num /= 5
                else:
                    return False
            return True
        elif num == 1:
            return True
        else:
            return False


solution = Solution()
print(solution.isUgly(214797179))
