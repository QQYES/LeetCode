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

        if t1 and not t2:
            tree_node = TreeNode(t1.val)
            if not t1.left or not t2.left:
                if t1.left:
                    tree_node.left = TreeNode(t1.left.val)
                elif t2.left:
                    tree_node.left = TreeNode(t2.left.val)
                else:
                    tree_node.left = None
            else:
                tree_node.left = TreeNode(t1.left.val + t2.left.val)
        elif t2 and not t1:
            tree_node = TreeNode(t2.val)
            if not t1.right or not t2.right:
                if t1.right:
                    tree_node.right = TreeNode(t1.right.val)
                elif t2.right:
                    tree_node.right = TreeNode(t2.right.val)
                else:
                    tree_node.right = None
            else:
                tree_node.right = TreeNode(t1.right.val + t2.right.val)
        elif not t1 and not t2:
            tree_node = None
        else:
            tree_node = TreeNode(t1.val + t2.val)
        if tree_node:
            self.mergeTrees(tree_node.left, tree_node.right)

        return tree_node
