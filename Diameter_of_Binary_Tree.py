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
        def get_depth(roots):
            """
            :param roots: TreeNode
            :return: int
            """
            if roots:
                l_depth = get_depth(roots.left)
                r_depth = get_depth(roots.right)
                if l_depth >= r_depth:
                    return l_depth + 1
                else:
                    return r_depth + 1
            else:
                return 0

        if root:
            count_l = get_depth(root.left)
            count_r = get_depth(root.right)
            return count_l + count_r
        else:
            return 0


solution = Solution()
tree_node = TreeNode(1)
tree_node.left = TreeNode(2)
tree_node.left.left = TreeNode(4)
tree_node.left.right = TreeNode(5)
tree_node.right = TreeNode(3)
res = solution.diameterOfBinaryTree(tree_node)
print(res)
