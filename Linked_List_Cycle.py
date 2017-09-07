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
        time = 0
        while head:
            head = head.next
            time += 1
            if time > 100000:
                return True
        return False


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
res = s.hasCycle(l)
print(res)
