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
        mem = set()
        while head:
            if head in mem:
                return True
            mem.add(head)
            head = head.next
        return False


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
res = s.hasCycle(l)
print(res)
