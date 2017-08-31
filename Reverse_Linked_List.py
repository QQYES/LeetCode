class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        if len(tmp) == 1:
            head = ListNode(tmp[0])
        elif len(tmp) > 0:
            last = ListNode(tmp[0])
            for i in range(1, len(tmp)):
                head = ListNode(tmp[i])
                head.next = last
                last = head
        return head


solution = Solution()
print(solution.reverseList(ListNode(1)))
