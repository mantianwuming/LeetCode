# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if head == None:
        #     return None
        # pre = ListNode(-1)
        # cur = head
        # pre.next = cur
        # while head != None and head.val == val:
        #     head = head.next
        #
        # while cur != None:
        #     if cur.val == val:
        #         pre.next = cur.next
        #         cur = cur.next
        #     else:
        #         pre = cur
        #         cur = cur.next
        # return head

        dummyHead = ListNode(-1)
        dummyHead.next = head
        cur = dummyHead;
        while cur.next != None:
            if cur.next.val == val:
                delNode = cur.next
                cur.next = delNode.next
                delNode.next = None
            else:
                cur = cur.next
        retNode = dummyHead.next
        return retNode
