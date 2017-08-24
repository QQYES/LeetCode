class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def visit(roots, count):
            """
            :param count: int
            :param roots: TreeNode
            :return: int
            """
            if roots:
                count += 1
                visit(roots.left, count)
                visit(roots.right, count)
            return count

        if root:
            count_l = visit(root.left, 0)
            count_r = visit(root.right, 0)
            return count_l + count_r + 1
