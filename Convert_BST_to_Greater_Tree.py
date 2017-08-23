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
        nodes = self.greater_add(root, [])
        s = []
        while root or s:
            while root:

                root.val += reduce(lambda x, y: x + y, [i for i in nodes if i > root.val])
                s.append(root)
                root = root.left

            if s:
                root = s.pop()
                root = root.right

        return root

    def greater_add(self, root, nodes):
        """
        :param root: TreeNode
        :param nodes: list
        :return: int
        """
        if root:
            nodes.append(root.val)
            if root.right:
                self.greater_add(root.right, nodes)
            if root.left:
                self.greater_add(root.left, nodes)
        return nodes


solution = Solution()
tree_node = TreeNode(5)
tree_node.left = TreeNode(2)
tree_node.right = TreeNode(13)
res = solution.convertBST(tree_node)
print(res.val, res.left.val, res.right.val)
