class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s_list = s.split(' ')
        for word in s_list:
            re_word = word[::-1]
            result.append(re_word)
        result = ' '.join(result)
        return result


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
