# Definition for a binary tree node.
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
        if root:
            root.val = self.greater_add(root, root.val)
            if root.right:
                self.convertBST(root.right)
            if root.left:
                self.convertBST(root.left)
        return root

    def greater_add(self, root, val):
        """
        :param root: TreeNode
        :param val: int
        :return: int
        """
        if root:
            if val < root.val:
                val += root.val
            if root.right:
                self.greater_add(root.right)
            if root.left:
                self.greater_add(root.left)
        return val

    def visit(self, root, nodes):
        """
        :param root: TreeNode
        :return: TreeNode
        """
        if root.left:
            self.visit(root.left, nodes)
        if root.right:
            self.visit(root.left, nodes)


solution = Solution()
tree_node = TreeNode(5)
tree_node.left = TreeNode(2)
tree_node.right = TreeNode(13)
res = solution.convertBST(tree_node)
print(res.val, res.left.val, res.right.val)
