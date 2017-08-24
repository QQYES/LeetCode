# Definition for a binary tree node.
from functools import reduce


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = root
        s = []
        sums = 0
        while root or s:
            while root:
                s.append(root)
                root = root.right
            if s:
                root = s.pop()
                root.val += sums
                sums = root.val
                root = root.left

        return res


solution = Solution()
tree_node = TreeNode(5)
tree_node.left = TreeNode(2)
tree_node.right = TreeNode(13)
res = solution.convertBST(tree_node)
print(res.val, res.left.val, res.right.val)
