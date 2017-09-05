class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def visit(root, l):
            """
            :param root: TreeNode
            :param l: str
            """
            if root:
                l += '^' + str(root.val) + '#'
                visit(root.left, l)
                visit(root.right, l)
            else:
                l += '$'

        s_list = ''
        t_list = ''
        visit(s, s_list)
        visit(t, t_list)
        if t_list in s_list:
            return True
        else:
            return False


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
