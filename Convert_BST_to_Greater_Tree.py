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

        if root.right:
            root.val += root.right.val
            return self.convertBST(root.right)

        if root.left:
            root.left.val += root.val
            return self.convertBST(root.left)


solution = Solution()
tree_node = TreeNode(5)
tree_node.left = TreeNode(2)
tree_node.right = TreeNode(13)
res = solution.convertBST(tree_node)
print(res.val, res.left.val, res.right.val)
