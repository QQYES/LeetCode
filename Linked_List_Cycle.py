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
        try:
            walker = head
            runner = head.next.next
            while walker and runner:
                if runner is walker:
                    return True
                walker = walker.next
                runner = runner.next.next
            return False
        except:
            return False


s = Solution()
l = ListNode(1)
l.next = l
res = s.hasCycle(l)
print(res)
