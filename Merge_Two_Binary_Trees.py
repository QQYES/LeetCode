class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            if t1:
                tree_node = t1
            elif t2:
                tree_node = t2
            else:
                tree_node = None
        else:
            tree_node = TreeNode(t1.val + t2.val)
            if t1.left or t2.left:
                if t1.left:
                    tree_node.left = TreeNode(t1.left.val)
                elif t2.left:
                    tree_node.left = TreeNode(t2.left.val)
                else:
                    tree_node.left = TreeNode(t1.left.val + t2.left)

            if t1.right or t2.right:
                if t1.right:
                    tree_node.right = TreeNode(t1.right.val)
                elif t2.right:
                    tree_node.right = TreeNode(t2.right.val)
                else:
                    tree_node.right = TreeNode(t1.right.val + t2.right.val)

        return tree_node
