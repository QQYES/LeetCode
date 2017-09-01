class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :param count:
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def compare(s_tree, t_tree):
            """
            :param s_tree: TreeNode
            :param t_tree: TreeNode
            :return: None
            """
            while s_tree and t_tree:
                if s_tree is None and t_tree is None:
                    return True
                if s_tree is None or t_tree is None:
                    return False
                if s_tree.val != t_tree.val:
                    return False
                return compare(s_tree.left, t_tree.left) and compare(s_tree.right, t_tree.right)

        if s is None:
            return False
        if compare(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


solution = Solution()
s = TreeNode(3)
s.left = TreeNode(4)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.right = TreeNode(5)
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
print(solution.isSubtree(s, t))
