# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        pre = None
        cur = head
        i = 1
        while i < m and cur != None:
            pre = cur
            cur = cur.next
            i += 1

        t1 = pre
        t2 = cur

        while i <= n and cur != None:
            next = cur.next

            cur.next = pre
            pre = cur
            cur = next
            i += 1

        if m == 1:
            t2.next = cur
            return pre

        t1.next = pre
        t2.next = cur
        return head
