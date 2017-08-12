class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        s_list = s.split(' ')
        for word in s_list:
            re_word = ''
            for char in list(word).__reversed__():
                re_word = re_word + char
            result = result + re_word + ' '
        print(result[:-1])


solution = Solution()
solution.reverseWords("Let's take LeetCode contest")
