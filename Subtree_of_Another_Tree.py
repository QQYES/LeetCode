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
        while s and t:
            if s.val == t.val:
                self.isSubtree(s.left, t.left)
                self.isSubtree(s.right, t.right)
            else:
                self.isSubtree(s.left, t)
                self.isSubtree(s.right, t)
        if t is None:
            return True
        else:
            return False
