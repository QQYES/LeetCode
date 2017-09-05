# Definition for a binary tree node.
from functools import reduce


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def sub_sum(r, l, sub_count, s):
            """
            :param sub_count: List
            :param r: TreeNode
            :param l: List
            :return:
            """

            if r:
                if len(l) != 0:
                    if reduce(lambda x, y: x + y, l) == s:
                        count.append(1)
                l.append(r.val)
                sub_sum(r.left, l, sub_count, s)
                sub_sum(r.right, l, sub_count, s)

        def visit(root, out_count, s):
            if root:
                l = []
                sub_sum(root, l, out_count, s)
                visit(root.left, out_count, s)
                visit(root.right, out_count, s)

        count = []
        visit(root, count, sum)
        if len(count) != 0:
            return reduce(lambda x, y: x + y, count)
        else:
            return 0


solution = Solution()
s = TreeNode(1)
print(solution.pathSum(s, 1))
