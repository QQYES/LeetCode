# Definition for singly-linked list.

import math


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mem = []
        while head:
            mem.append(head.val)
            head = head.next
        if len(mem) <= 1:
            return True
        if len(mem) > 1:
            if mem[:int((len(mem) / 2))] == [item for item in reversed(mem[int(round(len(mem) / 2)):])]:
                return True

        return False


s = Solution()
l = ListNode(1)
l.next = ListNode(0)
l.next.next = ListNode(1)
print(s.isPalindrome(l))
