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
        def get_depth(roots, sums):
            """
            :param sums: List
            :param roots: TreeNode
            :return: int
            """
            if roots:
                l_depth = get_depth(roots.left, sums)
                r_depth = get_depth(roots.right, sums)
                sums.append(l_depth + r_depth)
                return max(l_depth, r_depth) + 1
            else:
                return 0
        res = []
        get_depth(root, res)
        if res:
            return max(res)
        else:
            return 0


solution = Solution()
tree_node = TreeNode(1)
tree_node.left = TreeNode(2)
tree_node.left.left = TreeNode(4)
tree_node.left.right = TreeNode(5)
tree_node.right = TreeNode(3)
result = solution.diameterOfBinaryTree(tree_node)
print(result)
