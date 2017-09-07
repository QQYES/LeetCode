class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def init_tree(root, val):
    """
    :param val: int
    :param root: TreeNode
    :return: TreeNode
    """
    return TreeNode(val)


def run(l):
    head = TreeNode(None)
    for item in l :
        p=head
        root=TreeNode(item)

