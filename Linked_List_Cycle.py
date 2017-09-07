# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        mem = [head]
        while head:
            head = head.next

            if head not in mem:
                mem.append(head)
            else:
                return True
        return False


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
res = s.hasCycle(l)
print(res)
