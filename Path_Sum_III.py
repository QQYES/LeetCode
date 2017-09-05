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

        def sub_sum(r, l, sub_count, in_s):
            """
            :param in_s: List
            :param sub_count: List
            :param r: TreeNode
            :param l: List
            :return:
            """

            if r:
                sub_sum(r.left, l, sub_count, in_s)
                l.append(r.val)
                if reduce(lambda x, y: x + y, l) == in_s:
                    count.append(1)
                sub_sum(r.right, l, sub_count, in_s)

        def visit(out_root, out_count, s):
            if out_root:
                l = []
                sub_sum(out_root, l, out_count, s)
                visit(out_root.left, out_count, s)
                visit(out_root.right, out_count, s)

        count = []
        visit(root, count, sum)
        if len(count) != 0:
            return reduce(lambda x, y: x + y, count)
        else:
            return 0


solution = Solution()
s = TreeNode(10)
s.left = TreeNode(5)
s.left.left = TreeNode(3)
s.left.right = TreeNode(2)
s.left.left.left = TreeNode(3)
s.left.right.right = TreeNode(-2)

s.right = TreeNode(-3)
s.right.right = TreeNode(11)

print(solution.pathSum(s, 8))
