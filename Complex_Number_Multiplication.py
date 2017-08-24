class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        com_a = a.split('+')
        com_b = b.split('+')
        result = complex(int(com_a[0]), int(com_a[1].replace('i', ''))) * complex(int(com_b[0]),
                                                                                  int(com_b[1].replace('i', '')))
        # print result

        return str(int(result.real)) + '+' + str(int(result.imag)) + 'i'


solution = Solution()
print(solution.complexNumberMultiply("1+-1i", "2+-3i"))
