# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        l = ListNode(0)
        l.next = head
        dummyHead = l
        while l.next and l.next.next:
            m = l.next
            n = m.next
            o = n.next
            l.next = n
            n.next = m
            m.next = o
            l = m
        return dummyHead.next
