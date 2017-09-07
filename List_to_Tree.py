class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def run(l):
    queue = []
    head = TreeNode(l[0])
    queue.append(head)
    for index in range(1, len(l), 2):
        if l[index] != 'null':
            left = TreeNode(l[index])
        else:
            left = None
        queue.append(left)
        if l[index + 1] != 'null':
            right = TreeNode(l[index + 1])
        else:
            right = None
        queue.append(right)
        if len(queue) != 0:
            p = queue.pop(0)
            if p:
                p.left = left
                p.right = right
    return head


tree = run([10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1])
print(tree)
