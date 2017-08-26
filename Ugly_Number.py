from sympy import factor


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num == 1:
            return True
        else:
            while num > 1:
                for i in range(2, num + 1):
                    if num % i == 0:
                        if i not in (2, 3, 5):
                            return False
                        else:
                            num = int(num / i)
                            break
        return True


solution = Solution()
print(solution.isUgly(214797179))
