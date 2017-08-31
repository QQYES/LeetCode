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

        def visit(s_tree, t_tree, count):
            """
            :param s_tree: TreeNode
            :param t_tree: TreeNode
            :param count: List[int]
            :return: None
            """
            while s_tree and t_tree:
                if s_tree.val == t_tree.val:
                    count.insert(0, 1)
                    visit(s_tree.left, t_tree.left, count)
                    visit(s_tree.right, t_tree.right, count)
                else:
                    count.insert(0, 0)
                    visit(s_tree.left, t_tree, count)
                    visit(s_tree.right, t_tree, count)


        count = []
        visit(s, t, count)
        if count[0] == 1:
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
t.right = TreeNode(2)
t.left = TreeNode(1)
solution.isSubtree(s, t)
